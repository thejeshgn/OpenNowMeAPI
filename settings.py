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
"""
__version__ = "0.0.0"
__license__ = "GPLv3"
__author__ = "Thejesh GN <i@thejeshgn.com>"

import json

HOME_FOLDER = "./config/"

config_data = {}
with open(HOME_FOLDER+'nowme_config.json') as nowme_config_file:    
    config_data = json.load(nowme_config_file)

couchdb_username 		= config_data['couchdb_username'] 
couchdb_auth_username	= config_data['couchdb_auth_username'] 
couchdb_auth_password	= config_data['couchdb_auth_password'] 
couchdb_url				= config_data['couchdb_url'] 
report_sql_db_connection = "sqlite:///"+HOME_FOLDER+config_data["report_sql_db"] 


db_name_events=couchdb_username+"_events"
db_name_trackers=couchdb_username+"_trackers"
db_name_meta=couchdb_username+"_meta"

#as of now used only by SQL DB
db_name_notes=couchdb_username+"_notes"


db_full_url = "https://"+couchdb_auth_username+":"+couchdb_auth_password+"@"+couchdb_url
