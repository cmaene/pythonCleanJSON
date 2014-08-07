pythonCleanJSON
===============

Python version 2.7


# data source: 

https://datacatalog.cookcountyil.gov/Property-Taxation/Cook-County-Recorder-of-Deeds-Foreclosures-2011-Co/jr5c-gwim#SODA%20API

https://datacatalog.cookcountyil.gov/api/views/gac8-suhb/rows.json?accessType=DOWNLOAD


This parses, cleans, formats (see: _clean.json) and also save in CSV file (see: _clean.csv) using data I need from the cook county (powered by Socrata) JSON data - foreclosures in 2011. I was put off by the fact that Socrata data JSON format is NOT properly marked-up (no keys, just values most of the fields - below.) It is hard to deal with Socrata JSON without keys - i.e. they are so unlike JSONs by google or tweeter.. Note on the embedded quotes \" in address. I just don't like this JSON format!

# d = json.dumps(j2, indent=4) result below: 
(left# are the index # I figured out)

[
    [
0        1, 
1        "A20BFBBA-5D98-4553-B056-247F1314F191", 
2        1, 
3        1335364086, 
4        "395247", 
5        1335366041, 
6        "395247", 
7        "{\n}", 
8        "12-25-223-038-1009", 
9        "1100312136", 
10        "LIS PENDENS FORECLOSURE", 
11        "2011-01-03T00:00:00", 
12        "2010-12-27T00:00:00", 
13        null, 
14        [
            "{\"address\":\"2920 N HARLEM AVE\",\"city\":\"ELMWOOD PARK\",\"state\":\"IL\",\"zip\":\"60707-1226\"}", 
            "41.93338326917302", 
            "-87.80658083694772", 
            null, 
            false
        ]
    ], 