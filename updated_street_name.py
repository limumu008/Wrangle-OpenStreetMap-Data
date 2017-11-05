'''Improving the street name, mapping some '''
import xml.etree.cElementTree as ET
from collections import defaultdict
import re


SAMPLE_FILE = "sample_houston.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Avenue", "Boulevard", "Drive", "East", "Freeway", "Lane",
            "Parkway", "Plaza", "Road", "South", "Street", "West"]

# UPDATE THIS VARIABLE
mapping = { "Ave": "Avenue",
            "Blvd":"Boulevard",
           "Blvd.":"Boulevard",
           "Dr":"Drive",
           "Dr.":"Drive",
           "E": "East",
           "Frwy": "Freeway",
           "Fwy": "Freeway",
           "Ln":"Lane",
           "Pkwy":"Parkway",
           "pkwy": "Parkway",
           "Plaze":"Plaza",
           "Rd": "Road",
           "S":"South",
           "S.": "South",
           "St":"Street",
           "St.":"Street",
           "Stree":"Street",
           "W": "West"
            }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, mapping):
    '''Update the street name by using mapping dictionary'''
    m = street_type_re.search(name)
    if m:
        street_type = m.group()
        if street_type in mapping.keys():
            name = re.sub(street_type, mapping[street_type], name)
    return name


def output():
    st_types = audit(SAMPLE_FILE)
    #pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
        if name!=better_name:
            print (name, "=>", better_name)

if __name__ == '__main__':
     output()

