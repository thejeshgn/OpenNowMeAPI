# OpenNowMeAPI

An Open Framework for playing with [Nomie](https://nomie.io/) Tracker Events. 


# Install
- Clone the project
- `pip install -r requirements.txt`
- Edit `config/nowme_config.json` and add auth and couch db details



# To create a reporting 
- run `python batch_pull_data.py`
- It pulls the data from CouchDB and populates `config\report.sqlite'
- Table names depend on the `couchdb_username' like in Nomie couchdb setup

# SQL Tables
## TABLE username_trackers 

`
	id INTEGER NOT NULL, PRIMARY KEY
	lid TEXT, 
	stats TEXT, 
	min INTEGER, 
	color TEXT, 
	type TEXT, 
	_rev TEXT, 
	"dynamicCharge" BOOLEAN, 
	label TEXT, 
	charge INTEGER, 
	math TEXT, 
	groups TEXT, 
	max INTEGER, 
	_id TEXT, 
	config TEXT, 
	uom TEXT, 
	icon TEXT, 
	"ignoreZeros" BOOLEAN, 
	"chargeFunc" TEXT, 
`
## TABLE username_events
`
	id INTEGER NOT NULL, PRIMARY KEY
	doc TEXT, 
	_rev TEXT, 
	longitude FLOAT, 
	value TEXT, 
	latitude FLOAT, 
	_id TEXT, 
	time_ms INTEGER, 
	tracker_id TEXT, 
	charge INTEGER, 
	timestamp DATETIME
`
