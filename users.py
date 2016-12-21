# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:02:35 2016

@author: Gaoyuan
"""
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    return


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        try:
            uid = element.attrib['uid']
            users.add(uid)
        except KeyError:
            pass
    return users


def test():

    users = process_map('sample.osm')
    pprint.pprint(users)
    #assert len(users) == 6



if __name__ == "__main__":
    test()