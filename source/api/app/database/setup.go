package database

import "gopkg.in/mgo.v2"

/*
Database session
*/
var Session *mgo.Session

/*
Commits's model connection
*/
var Commits *mgo.Collection

/*
Init database
*/
func Init(uri, dbname string) error {
	session, err := mgo.Dial(uri)
	if err != nil {
		return err
	}

	session.SetMode(mgo.Monotonic, true)

	// Expose session and models
	Session = session
	Commits = session.DB(dbname).C("commits")

	return nil
}
