from bs4 import beautifulSoup
with open("example.xml") as fp:
    soup = BeautifulSoup(fp, 'xml')

root_tag = soup.find('schedule')
root_childs = [e.name for e in root_tag.descendants if e.name is not None]
print(root_childs)
