from bs4 import BeautifulSoup
import requests

#* Git URL and soup content from search input
def getSearch(passSearch):
    website = requests.get('https://stackoverflow.com/questions/tagged/' + passSearch + '?sort=MostVotes&edited=true')
    soup = BeautifulSoup(website.content, 'html.parser')
    return soup

def getHeadings(passData):
    headings = passData.find_all('h3', class_ = 's-post-summary--content-title')
    return headings

def getSummaries(passData):
    summaries = passData.find_all('div', class_ = 's-post-summary--content-excerpt')
    return summaries

def getUrls(passData):
    urls = passData.find_all('a', class_ = 's-link', href=True)
    return urls

def getStats(passData):
    stats = passData.find_all('span', class_ = 's-post-summary--stats-item-number')
    return stats

def buildUrls(urls):
    link1 = 'https://stackoverflow.com' + urls[3].get('href')
    link2 = 'https://stackoverflow.com' + urls[4].get('href')
    link3 = 'https://stackoverflow.com' + urls[5].get('href')
    link4 = 'https://stackoverflow.com' + urls[6].get('href')
    link5 = 'https://stackoverflow.com' + urls[7].get('href')
    link6 = 'https://stackoverflow.com' + urls[8].get('href')
    link7 = 'https://stackoverflow.com' + urls[9].get('href')
    link8 = 'https://stackoverflow.com' + urls[10].get('href')
    link9 = 'https://stackoverflow.com' + urls[11].get('href')
    link10 = 'https://stackoverflow.com' + urls[12].get('href')
    return link1, link2, link3, link4, link5, link6, link7, link8, link9, link10