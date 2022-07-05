from lxml import etree
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


# If XML is not in proper structure run these code
# with open("example.xml") as fp:
#     soup = BeautifulSoup(fp, 'xml')
# pretty_xml = soup.prettify()
# with open("example2.xml", "w") as writter:
#     writter.write(pretty_xml)



def etree_iter_path(node, tag=None, path='schedule'):
    if tag is None or node.tag == tag:
        yield node, path
    for child in node:
        _child_path = '%s/%s' % (path, child.tag)
        for child, child_path in etree_iter_path(child, tag, path=_child_path):
            yield child, child_path
xmldoc = ElementTree.parse("mproschedule 05042020.xml")
xml_schema = set()
for elem, path in etree_iter_path(xmldoc.getroot()):
    for element in xmldoc.iter(path.split('/')[-1]):
        for key in element.attrib:
            xml_schema.add(path)
            xml_schema.add(path+"/@"+key)
print(sorted(xml_schema, key=len))
