package controllers

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"

	"github.com/rafalgolarz/BackEndTest/source/api/app/database"
	"github.com/rafalgolarz/BackEndTest/source/api/app/models"
	"github.com/revel/revel"
	"gopkg.in/mgo.v2/bson"
)

/*
Commits controller
*/
type Commits struct {
	*revel.Controller
}

/*
Index of all commits
*/
func (c Commits) Index() revel.Result {
	results := []models.Commit{}
	if err := database.Commits.Find(bson.M{}).All(&results); err != nil {
		// Internal Server Error
		log.Fatal(err)
	}
	return c.RenderJSON(results)
}

/*
Show particular commit
*/
func (c Commits) Author(author string) revel.Result {
	results := []models.Commit{}
	if err := database.Commits.Find(bson.M{"author": author}).All(&results); err != nil {
		// Internal Server Error
		log.Fatal(err)
	}
	return c.RenderJSON(results)
}

/*
Add commit
*/
func (c Commits) Add(id string) revel.Result {
	commit := &models.Commit{}
	if body, err := ioutil.ReadAll(c.Request.Body); err != nil {
		return c.RenderText("add: bad request")

	} else if err := json.Unmarshal(body, commit); err != nil {
		return c.RenderText("add: could not parse request")

	} else if err := database.Commits.Insert(commit); err != nil {
		// Internal Server Error
		//log.Fatal(err)
		c.Response.Status = http.StatusInternalServerError
		return c.RenderText("add: could not be saved")
	}
	c.Response.Status = http.StatusCreated
	return c.RenderJSON(commit)
}

/*
Update commit
*/
func (c Commits) Update(id string) revel.Result {
	commit := &models.Commit{}
	result := models.Commit{}
	obj := bson.ObjectIdHex(id)

	if !bson.IsObjectIdHex(id) {
		c.Response.Status = http.StatusBadRequest
		return c.RenderText("id is not valid")

	} else if !obj.Valid() {
		c.Response.Status = http.StatusBadRequest
		return c.RenderText("id is not valid")
	} else if err := database.Commits.Find(bson.M{"_id": obj}).One(&result); err != nil {
		// Internal Server Error
		log.Fatal(err)
	} else if body, err := ioutil.ReadAll(c.Request.Body); err != nil {
		return c.RenderText("bad request")

	} else if err := json.Unmarshal(body, commit); err != nil {
		return c.RenderText("update: could not parse request")
	}

	//update only the reviewed field
	reviewed := commit.Reviewed
	commit = &result
	commit.Reviewed = reviewed

	if err := database.Commits.UpdateId(obj, commit); err != nil {
		// Internal Server Error
		log.Fatal(err)
		c.Response.Status = http.StatusInternalServerError
		return c.RenderText("could not be updated")
	}

	return c.RenderJSON(commit)
}
