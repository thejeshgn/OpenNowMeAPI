# -*- coding: utf-8 -*-

"""
Copyright 2017 Thejesh GN <i@thejeshgn.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

DATABASE TABLES
username_events 	-- storage for all events (tracker taps, notes, and more coming soon) 
						are stored in the this database. 
username_trackers	-- storage for all trackers
username_meta 		-- storage for group data, favorite comparisons, preferences, etc.

"""

__version__ = "0.0.0"
__license__ = "GPLv3"
__author__ = "Thejesh GN <i@thejeshgn.com>"


import sys, os
sys.path.append(os.path.dirname(__file__))

import couch_database
import sql_database
import json
import datetime


def pull_trackers():
	"""Given a label gets the tracker"""
	results = couch_database.getAllTrackers()
	for row in results:
		doc 	=  row['doc']	
		_id 	= doc['_id']
		_rev 	= doc['_rev']

		db_row_id_rev = sql_database.getTrackerByIdAndRev(_id=_id, _rev=_rev)
		if db_row_id_rev:
			print "specific version exists so do nothing"
			continue
		else:

			#1. Set all config values into main document
			config = doc['config']
			doc['type'] =  config['type']
			if config.has_key('uom'):
				doc['uom'] =  config['uom']		
			if config.has_key('math'):
				doc['math'] =  config['math']
			if config.has_key('dynamicCharge'):
				doc['dynamicCharge'] =  config['dynamicCharge']
			if config.has_key('ignoreZeros'):
				doc['ignoreZeros'] =  config['ignoreZeros']
			if config.has_key('min'):
				doc['min'] =  config['min']
			if config.has_key('max'):
				doc['max'] =  config['max']
			if config.has_key('chargeFunc'):
				doc['chargeFunc'] =  json.dumps(config['chargeFunc'])
			
			#also store json
			if doc.has_key('stats'):
				doc['stats'] = json.dumps(doc['stats'])
			doc['config'] = json.dumps(config)
			groups = doc['groups']
			doc['groups'] = json.dumps(groups)

			sql_database.addOrUpdateTracker(doc)


def pull_events():
	limit = 4000
	skip = 0

	while(1):
		results = couch_database.getAllEvents(limit=limit, skip=skip)
		skip = skip + limit		
		if len(results) == 0:
			#break while loop
			break

		for row in results:		
			_id = row["id"]
			value = row['value']
			_rev = value['rev']
			print str(_id)

			if not str(_id).startswith("tick|pr|"):
				print "skipping"
				continue

			if sql_database.getEventByIdandRev(_id=_id, _rev=_rev):
				#latest exists, do nothing
				print "latest exists"
				pass
			else:					
				document = couch_database.getSingleEvent(_id)
				doc = {}
				doc["_id"] = document["_id"]
				doc["_rev"] = document["_rev"]

				parts = _id.split("|")
				tracker_id = parts[2]
				time_ms = int(parts[3])
				print str(time_ms)
				charge = int(parts[4])

				doc["tracker_id"] = tracker_id
				doc["time_ms"] = time_ms
				doc["timestamp"] = datetime.datetime.fromtimestamp(time_ms/1000.0)
				doc["charge"] = charge


				if document.has_key('value'):
					doc["value"] = str(document["value"])
				if document.has_key('geo'):
					geo = document['geo']
					if geo and len(geo) > 0:
						latitude = geo[0]
						longitude = geo[1]
						doc["latitude"]=latitude
						doc["longitude"]=longitude
				doc['doc']= json.dumps(document)
				print "Add/Update"	
				print sql_database.addOrUpdateEvent(doc)

if __name__== "__main__":
	pull_trackers()
	pull_events()
