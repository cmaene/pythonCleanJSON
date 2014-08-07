pythonCleanJSON
===============

Python version 2.7

## See:
 -  Main file: foreclosures.py
 -  Output file (json): foreclosures2011_clean.json
 -  Output file (csv) : foreclosures2011_clean.csv


### data source: 
https://datacatalog.cookcountyil.gov/Property-Taxation/Cook-County-Recorder-of-Deeds-Foreclosures-2011-Co/jr5c-gwim#SODA%20API

https://datacatalog.cookcountyil.gov/api/views/gac8-suhb/rows.json?accessType=DOWNLOAD


### why I made this..
This parses, cleans, formats (see: _clean.json) an input JSON file and also save
it in the CSV format(see: _clean.csv) using data from Cook county's data portal
(powered by Socrata). I was put off by the fact that Socrata's JSON format is NOT
properly marked-up (no keys, just values most of the fields. It is hard to deal
with JSON without keys - i.e. Socrata's JSON is so unlike JSONs by google or tweeter..
Note on the embedded quotes \" in address. I just don't like Socrata's JSON format!