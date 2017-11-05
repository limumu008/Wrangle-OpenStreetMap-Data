'''Update the zipcode'''
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSM_FILE = "Houston.osm"  
SAMPLE_FILE = "sample_houston.osm"

def audit_zipcode(zipcode_types, zipcode_name):
	
	if not (re.match(r'^(78|76)\d{3}$', zipcode_name)):
		zipcode_types[zipcode_name].add(zipcode_name)

def is_zipcode(elem):
	
	return (elem.attrib['k'] == "addr:postcode")

def audit(osmfile):
	
	osm_file = open(osmfile, "r")
	zipcode_types = defaultdict(set)
	for event, elem in ET.iterparse(osm_file, events=("start",)):
		if elem.tag == "node" or elem.tag == "way":
			for tag in elem.iter("tag"):
				if is_zipcode(tag):
					audit_zipcode(zipcode_types, tag.attrib['v'])
	elem.clear()
	return zipcode_types

def update_zipcode(zip):
	
	char = re.findall('[a-zA-z]*', zip)
	if char:
		char = char[0]
	char = char.strip()
	if char == "TX" or "tx":
		better_zip = re.findall(r'\d+', zip)
		if better_zip:
			if len(better_zip) == 2:
				return better_zip[0]
			else:
				return better_zip
	else:
		better_zip = re.findall(r'\d+', zip)
		if better_zip:
			if len(better_zip) == 2:
				return better_zip[0]
			else:
				return better_zip

def output():
    
    zipcodes = audit(SAMPLE_FILE)
    pprint.pprint(dict(zipcodes))

    for zipcode, ways in zipcodes.iteritems():
        for name in ways:
            better_name = update_zipcode(name)
        if name!=better_name:
            print (name, "=>", better_name)

if __name__ == '__main__':
     output()


