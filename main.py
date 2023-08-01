from scripts.search import search
from scripts.data import *

passSearch = search()
passData = getSearch(passSearch)
headings = getHeadings(passData)

#! Delete after Testing - Prints first 5 Headings
print(headings[0].text)
print(headings[1].text)
print(headings[2].text)
print(headings[3].text)
print(headings[4].text)

