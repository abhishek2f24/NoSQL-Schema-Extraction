from bs4 import beautifulSoup
with open("example.xml") as fp:
     soup = BeautifulSoup(fp, 'xml')
for child in soup.recursiveChildGenerator():
    if child.name:
        print(child.name)
        child = child.findChildren()for child in soup.recursiveChildGenerator():
    
