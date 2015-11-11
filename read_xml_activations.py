#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

# calling the main function:


def main():
    print "Program name: ", sys.argv[0]
    print "passed argument to XML parser: ", sys.argv[1]
    parseXML(sys.argv[1])

# example for a user defined function:
# parsing an XML file getting the name of the tag 'model'

def parseXML(s):
    tree = ET.parse(s)
    root = tree.getroot()

    for element in root.iter('model'):
        print element.text


if __name__ == '__main__':
    main()