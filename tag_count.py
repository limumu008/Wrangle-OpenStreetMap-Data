'''Count the number of tags'''

import xml.etree.ElementTree as ET
import pprint

OSM_FILE = "Houston.osm"  # Replace this with your osm file
SAMPLE_FILE = "sample_houston.osm"

def count_tags(filename):
    ans = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag not in ans.keys():
            ans[elem.tag] = 1
        else:
            num_elem = ans[elem.tag] + 1
            ans[elem.tag] = num_elem
    return ans

pprint.pprint(count_tags(SAMPLE_FILE))