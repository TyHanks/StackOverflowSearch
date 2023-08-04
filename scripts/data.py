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

#def getUrls(passData):
#
#    return urls

#def getVotes(passData):

#    return votes

#def getAnswers(passData):

#    return answers

#def getViews(passData):

#    return views