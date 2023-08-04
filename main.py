from scripts.search import search
from scripts.data import *

passSearch = search()
passData = getSearch(passSearch)
headings = getHeadings(passData) #* headings[0].string 0 thru 9
summaries = getSummaries(passData) #* summaries[0].string 0 thru 9
urls = getUrls(passData)
useableUrls = buildUrls(urls) #* useableUrls[0] 0 thru 9
stats = getStats(passData) #* stats[0].string // 0,1,2 = votes,answers,views 3,4,5 = votes,answers,views etc...


