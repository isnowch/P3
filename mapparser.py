# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:52:49 2016

@author: Gaoyuan
"""

import xml.etree.cElementTree as ET
import pprint
'''
for event, elem in ET.iterparse('example.osm'):
    print elem.tag
'''
def count_tags(filename):
    tags_count = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag in tags_count.keys():
            tags_count[elem.tag] += 1
        else:
            tags_count[elem.tag] = 1
    return tags_count
     


def test():

    tags = count_tags('sample.osm')
    pprint.pprint(tags)
'''
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}
'''
    

if __name__ == "__main__":
    test()