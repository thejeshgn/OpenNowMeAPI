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


import couchdb
import json
import time
import settings

#READ THESE FROM CONFIG


couch = couchdb.Server(settings.db_full_url)
couchdb_db_events 	= couch[settings.db_name_events]
couchdb_db_trackers	= couch[settings.db_name_trackers]

def getTracker(label):
	"""Given a label gets the tracker"""
	results = couchdb_db_trackers.view('_all_docs',wrapper=None,include_docs=True)
	for row in results:
		if row['doc']['label'] == label:
			return row['doc']

def getAllTrackers():
	return couchdb_db_trackers.view('_all_docs',wrapper=None,include_docs=True)


def getAllEvents(limit=4000, skip=0):
	startkey= '"tick|pr|"'
	endkey= '"tick|pr|香"'
	return couchdb_db_events.view('_all_docs',wrapper=None,start_key=startkey,end_key=endkey,inclusive_end=True, limit=limit, skip=skip)

def getSingleEvent(_id):
	return couchdb_db_events[_id]

