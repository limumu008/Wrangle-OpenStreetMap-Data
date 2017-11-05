'''Auditing the different types of keys'''
import xml.etree.ElementTree as ET
import re

OSM_FILE = "Houston.osm"  # Replace this with your osm file
SAMPLE_FILE = "sample_houston.osm"

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    if element.tag == "tag":
        m = lower.search(element.attrib['k'])
        n = lower_colon.search(element.attrib['k'])
        o = problemchars.search(element.attrib['k'])
        if m:
            keys["lower"] += 1
        elif n:
            keys["lower_colon"]+=1
        elif o:
            keys["problemchars"]+=1
        else:
            keys["other"]+=1
    return keys



def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)
    print keys
    return keys

if __name__ == "__main__":
    process_map(SAMPLE_FILE)