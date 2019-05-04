from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.wikipedia.org/")
bsobject = BeautifulSoup(html.read(), "html.parser")
print(bsobject.title)
