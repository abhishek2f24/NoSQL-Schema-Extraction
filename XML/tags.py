import xml.etree.ElementTree as ET

def perf_func(elem, func, level=0):
    func(elem,level)
    for child in elem.getchildren():
        perf_func(child, func, level+1)

def print_level(elem,level):
    print('-'*level+elem.tag)

root = ET.parse('example2.xml')
perf_func(root.getroot(), print_level)
