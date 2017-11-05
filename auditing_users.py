'''Explore the users and count the number of users.'''

import xml.etree.ElementTree as ET

OSM_FILE = "Houston.osm"  # Replace this with your osm file
SAMPLE_FILE = "sample_houston.osm"

def get_user(element):
    if 'uid' in element.attrib:
        user = element.get('uid')
        return user


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        user = get_user(element)
        if user != None :
            users.add(user)
    return users

print "The number of different users is "+str(len(process_map(SAMPLE_FILE)))