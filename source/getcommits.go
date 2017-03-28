package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strings"
	"time"
)

//-----------------------------------------------------
// Structres reflect github API commits structer
// Needed to decode JSON into proper data fields
//-----------------------------------------------------

type CommitType struct {
	Sha       string        `json:"sha"`
	Url       string        `json:"url"`
	Html_url  string        `json:"html_url"`
	Author    AuthorObj     `json:"author"`
	Committer CommitterObj  `json:"committer"`
	Tree      TreeObj       `json:"tree"`
	Message   string        `json:"message"`
	Parrents  ParrentsArray `json:"parrents"`
}

type AuthorObj struct {
	Name  string `json:"name"`
	Email string `json:"email"`
	Date  string `json:"date"`
}

type CommitterObj struct {
	Name  string `json:"name"`
	Email string `json:"email"`
	Date  string `json:"date"`
}

type TreeObj struct {
	Sha string `json:"sha"`
	Url string `json:"url"`
}

type ParrentsArray []Parrent

type Parrent struct {
	Sha      string `json:"sha"`
	Url      string `json:"url"`
	Html_url string `json:"html_url"`
}

/*
 * Urls that store details about a commit (url per commit)
 */
type CommitUrls struct {
	Commit CommitUrl
}
type CommitUrl struct {
	Url string `json:"url"`
}

var myClient = &http.Client{Timeout: 10 * time.Second}

//-------------------------------------------------------------------

/**
 * Download any JSON content from the url am
 */

func getJson(url string, target interface{}) error {
	response, err := myClient.Get(url)
	if err != nil {
		return err
	}
	defer response.Body.Close()

	return json.NewDecoder(response.Body).Decode(target)
}

/**
 * Download any sort of content from the url
 */

func getContent(url string) []byte {
	resp, err := myClient.Get(url)
	if err != nil {
		return nil
	}
	defer resp.Body.Close()
	res, err := ioutil.ReadAll(resp.Body)
	log.Println(err)
	return res
}

//-------------------------------------------------------------------

var listOfUrls [NUMBER_OF_COMMITS]string

const COMMITS_URL = "https://api.github.com/repos/nodejs/node/commits?page=1&per_page=25"
const POST_URL = "http://localhost:9000/commits/add"
const NUMBER_OF_COMMITS = 25

func main() {

	//-------------------------------------------------------
	// DOWNLOADING URLS REPRESENTING EACH OF THE LAST COMMITS
	//-------------------------------------------------------

	var lastCommits []byte
	//load commits from the static file if you exceeded the limit (60req/h from 1 IP)
	//lastCommits, _ = ioutil.ReadFile("./sample.json")
	lastCommits = getContent(COMMITS_URL)
	fmt.Printf("Downloaded content %v\n", string(lastCommits))

	var urls []CommitUrls
	json.Unmarshal(lastCommits, &urls)

	var numberOfurls = len(urls)
	var toDownload = 0
	if numberOfurls > 0 {
		if numberOfurls >= NUMBER_OF_COMMITS {
			toDownload = NUMBER_OF_COMMITS
		} else {
			toDownload = numberOfurls
		}
		for i := 0; i < toDownload; i++ {
			listOfUrls[i] = urls[i].Commit.Url
			//fmt.Println(listOfUrls[i])
		}
	} else {
		log.Println("Cannot get any commits to download")
	}

	//----------------------------------------------------
	// CALLING THE API TO ADD DOWNLOADED COMMITS TO THE DB
	//----------------------------------------------------
	var commitJson CommitType
	var singleCommit []byte
	if toDownload > 0 {

		for j := 0; j < toDownload; j++ {
			fmt.Println("Downloading: ", listOfUrls[j])
			// singleCommit, _ = ioutil.ReadFile("./commit2.json")
			getJson(listOfUrls[j], &commitJson)
			json.Unmarshal(singleCommit, &commitJson)

			if commitJson.Sha != "" {
				//prepare JSON POST body
				var post_data string = "{\"sha\": \"" + commitJson.Sha +
					"\", \"author\": \"" + commitJson.Author.Name +
					"\", \"committer\": \"" + commitJson.Committer.Name +
					"\", \"date\":\"" + commitJson.Committer.Date +
					"\", \"message\":\"" + commitJson.Message[:25] + "..." +
					"\", \"url\": \"" + commitJson.Url +
					"\", \"reviewed\": false}"

				client := &http.Client{}
				req, _ := http.NewRequest("POST", POST_URL, strings.NewReader(post_data))
				req.Header.Add("Content-Type", "application/json; charset=utf-8")

				//show the body request
				fmt.Printf("%v", post_data)

				resp, _ := client.Do(req)
				fmt.Println(resp.Status)
			} else {
				log.Println("Empty response. Probably the API rate limit exceeded for your IP")
			}
		}
	}

}
