# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:04:39 2016

@author: Gaoyuan
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "sample.osm"
en_name_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Expressway","Bridge", "Hospital", "Institute", "Line", "Railway","River",'School','Station','Statium','Tower','Town','University']
expected_city = [u"天津市", u"北京市", u"Tianjin", u"Beijing", u"Tangshan"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
            "Rd": "Road",
            "Lu": "Road",
            "Dao": "Road",
            "Xian": "Line",
            "lu": "Road",
            "RD": "Road",
            "Qiao": "Bridge",
            "Hospita": "Hospital",
            "Road)": "Road"
            }

mapping_city = {"tianjin": "Tianjin",
                "Tianjin/China": "Tianjin",
                u"天津": u"天津市",
                u"北京": u"北京市"             
                }


def audit_en_name(en_names, en):
    m = en_name_re.search(en)
    if m:
        en_name = m.group()
        if en_name not in expected:
            en_names[en_name].add(en)

def audit_city_name(city_names, city_name):
    if city_name not in expected_city:
        city_names.add(city_name)

def is_en_name(elem):
    return (elem.attrib['k'] == "name:en")

def is_city_name(elem):
    return (elem.attrib['k'] == "addr:city")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    en_names = defaultdict(set)
    city_names = set()
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_en_name(tag):
                    audit_en_name(en_names, tag.attrib['v'])
                if is_city_name(tag):
                    audit_city_name(city_names, tag.attrib['v'])
    return en_names, city_names
    osm_file.close()


def update_en_name(name, mapping):
    road_cn = ['lu', 'Lu', 'Dao','dao']
    
    n = en_name_re.search(name).group()
    if n in mapping.keys():
        name = name.replace(n, mapping[n])
        
    for e in road_cn:
        if name.find(e) == len(name) - len(e):
            name = name.replace(e, ' Road')
            
    if name.find('qiao') == len(name) - len('qiao'):
            name = name.replace('qiao', ' Bridge')
            
    return name

def update_city_name(name, mapping_city):
    if name in mapping_city.keys():
        name = mapping_city[name]
    return name


def test():
    en_names, city_names = audit(OSMFILE)
    #assert len(st_types) == 3
    pprint.pprint(dict(en_names))
    
    for name, addrs in en_names.iteritems():
        for name in addrs:
            better_name = update_en_name(name, mapping)
            print name, "=>", better_name
    
    for name in city_names:
        better_name = update_city_name(name, mapping_city)
        print name, "=>", better_name


if __name__ == '__main__':
    test()
