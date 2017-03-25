package models

import "gopkg.in/mgo.v2/bson"

/*
commit model
*/
type Commit struct {
	ID        bson.ObjectId `json:"_id,omitempty" bson:"_id,omitempty"`
	Sha       string        `json:"sha" bson:"sha"`
	Author    string        `json:"author" bson:"author"`
	Committer string        `json:"committer,omitempty" bson:"committer,omitempty"`
	Date      string        `json:"date" bson:"date"`
	Message   string        `json:"message" bson:"message"`
	URL       string        `json:"url" bson:"url"`
	Reviewed  bool          `json:"reviewed" bson:"reviewed"`
}
