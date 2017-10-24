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

import settings
import dataset
import json
import datetime


sql_db = dataset.connect(settings.report_sql_db_connection)


def getAllTrackers():
	sql_table_trackers = sql_db[settings.db_name_trackers]
	return sql_table_trackers


def getTracker(label):
	sql_table_trackers = sql_db[settings.db_name_trackers]
	return sql_table_trackers.find_one(label=label)


def getTrackerByIdAndRev(_id, _rev):
	sql_table_trackers = sql_db[settings.db_name_trackers]
	db_row_id_rev = sql_table_trackers.find_one(_id=_id, _rev=_rev)
	return db_row_id_rev


def addOrUpdateTracker(doc):
	sql_table_trackers = sql_db[settings.db_name_trackers]
	return  sql_table_trackers.upsert(doc,['_id'])	


def getEventByIdandRev(_id, _rev):
	sql_table_events = sql_db[settings.db_name_events]	
	return sql_table_events.find_one(_id=_id, _rev=_rev)


def addOrUpdateEvent(doc):
	sql_table_events = sql_db[settings.db_name_events]
	return sql_table_events.upsert(doc,['_id'])
