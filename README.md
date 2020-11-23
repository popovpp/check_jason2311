# check_jason2311
Script "check_json2311.py" das check of json files with filename extension ".json"  by jsonschema files with filename extension ".schema".
Script must be in folder has subfolders /event/ and /schema/.
Json files must be in folder /event/ always.
Jsonschema files must be in folder /schema/ always.
Script checks each json file in folder /event/ by each jsonschema files in folder /schema/.
Script made by Python 3.8.
Startup syntax:
\python check_json2311.py
Script work result is log-file has name of json file and filename extension ".log"

Format of log-file is showed below.
 
json -  3ade063d-d1b9-453f-85b4-dda7bfda4711.json

schema -  cmarker_created.schema

....FIELD NAME...|......LOCATION......|.VALIDITY.|....YOU CAN FIND FIELD...|.............RECOMENDATIONS.............

id...............|in json {root}......|Invalid...|in json {"data" {} }.....|MOVE the field to the json {root} ......
user_id..........|in everywhere.......|Valid.....|.........................|........................................
event............|in json {root}......|Invalid...|.........................|ADD the field in the schema or REMOVE field
data.............|in json {root}......|Invalid...|.........................|ADD the field in the schema or REMOVE field
created_at.......|in json {root}......|Invalid...|.........................|ADD the field in the schema or REMOVE field
environment_id...|in json {root}......|Invalid...|.........................|ADD the field in the schema or REMOVE field
cmarkers.........|in schema {proper}..|..........|in json {"data" {} }.....|MOVE the required field to the json {root}
datetime.........|in schema {proper}..|..........|.........................|ADD the required fiels in the json {root}

schema -  label_selected.schema

....FIELD NAME...|......LOCATION......|.VALIDITY.|....YOU CAN FIND FIELD...|.............RECOMENDATIONS.............

id...............|in everywhere.......|Invalid...|in json {"data" {} }.....|MOVE the field to the json {root} CONTROL type or limits of the field
user_id..........|in everywhere.......|Valid.....|.........................|........................................
event............|in json {root}......|Invalid...|.........................|ADD the field in the schema or REMOVE field
data.............|in json {root}......|Invalid...|.........................|ADD the field in the schema or REMOVE field
created_at.......|in json {root}......|Invalid...|.........................|ADD the field in the schema or REMOVE field
environment_id...|in json {root}......|Invalid...|.........................|ADD the field in the schema or REMOVE field
user.............|in schema {proper}..|..........|.........................|ADD the required fiels in the json {root}
rr_id............|in schema {proper}..|..........|.........................|ADD the required fiels in the json {root}
labels...........|in schema {proper}..|..........|.........................|ADD the required fiels in the json {root}
timestamp........|in schema {proper}..|..........|.........................|ADD the required fiels in the json {root}
unique_id........|in schema {proper}..|..........|.........................|ADD the required fiels in the json {root}
