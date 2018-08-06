import sys
import xml.etree.ElementTree as ET

XML_FILE = sys.argv[1]

tree = ET.parse(XML_FILE)
root = tree.getroot()

elem = []
for child in root:
	elem = set([x.tag for x in root.findall(child.tag+"/*")]) 
  #this also can be written as elem = {x.tag for x in root.findall(child.tag+"/*")]}

print("Elements of the given xml - " ,elem)
