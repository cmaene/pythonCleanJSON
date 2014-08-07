pythonCleanJSON
===============

Python version 2.7

## see the python script: foreclosures.py


### data source: 

https://datacatalog.cookcountyil.gov/Property-Taxation/Cook-County-Recorder-of-Deeds-Foreclosures-2011-Co/jr5c-gwim#SODA%20API

https://datacatalog.cookcountyil.gov/api/views/gac8-suhb/rows.json?accessType=DOWNLOAD


This parses, cleans, formats (see: _clean.json) and also save in CSV file (see: _clean.csv) using data I need from the cook county (powered by Socrata) JSON data - foreclosures in 2011. I was put off by the fact that Socrata data JSON format is NOT properly marked-up (no keys, just values most of the fields - below.) It is hard to deal with Socrata JSON without keys - i.e. they are so unlike JSONs by google or tweeter.. Note on the embedded quotes \" in address. I just don't like this JSON format -