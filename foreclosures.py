""" python version 2.7
# data source: 
https://datacatalog.cookcountyil.gov/Property-Taxation/Cook-County-Recorder-of-Deeds-Foreclosures-2011-Co/jr5c-gwim#SODA%20API
https://datacatalog.cookcountyil.gov/api/views/gac8-suhb/rows.json?accessType=DOWNLOAD

This parses, cleans, formats (see: _clean.json) an input JSON file and also saves
it in the CSV format(see: _clean.csv) using data from Cook county's data portal
(powered by Socrata). I was put off by the fact that Socrata's JSON format is NOT
properly marked-up (no keys, just values most of the fields. It is hard to deal
with JSON without keys - i.e. Socrata's JSON is so unlike JSONs by google or tweeter..
Note on the embedded quotes \" in address. I just don't like Socrata's JSON format!
 
# d = json.dumps(j2, indent=4) result below: (left# are the index # I figured out)
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
"""
import sys, os, json, csv

def main():
    temp = {}
    #dic  = {} # don't create a dictionary here as we want a new dic for each line later
    diclist = []
    with open(sys.argv[1],'r') as f:
	inputfname = os.path.splitext(os.path.basename(sys.argv[1]))[0]
        j = json.load(f)
        j2=j["data"]
        d = json.dumps(j2)
        '''file = open(inputfname+'_dataonly.txt',"w") # if you want to save data section
	file.write(d)
        file.close'''
	temp = json.loads(d) # I only need the "data" section
	file =  open(inputfname+'_clean.json',"w") # process each line and save
	for line in temp:
    	    dic  = {} # here - this is where we create a new dictionary
	    dic["sid"] = line[0]
	    dic["pin"] = line[8]
	    dic["docnum"] = line[9]
	    dic["doctype"] = line[10]
	    dic["recorddate"] = line[11]
	    dic["address"] = line[14][0]
	    # address fields are hard to split, you know why? because Socrata embeds quotes
	    # with escape\, making look like key-value but are NOT; no index, just chars
	    dic["lat"] = line[14][1]
	    dic["lon"] = line[14][2]
	    # if "\n" in line[7]:
	    file.write(json.dumps(dic, sort_keys=True)+"\n") # writes each dictionary..
	    diclist.append(dic)
        file.close
        '''for row in diclist: # for output checking
	    print row'''
	# Also save it the list of dictionaries in CSV format
 	fnames = sorted(list(set(k for d in diclist for k in d))) # list of field names
    	with open(inputfname+'_clean.csv', 'wb') as f2:  
	    w = csv.DictWriter(f2, fieldnames=fnames)
	    w.writeheader()
	    for row in diclist:
	        w.writerow(row)
	file.close

# =============================
if __name__ == '__main__':
  #inputdata = open(sys.argv[1])
  main()
