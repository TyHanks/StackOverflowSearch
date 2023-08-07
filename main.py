import sys
import os
from scripts.data import *
from pyfiglet import Figlet
from clint.textui import prompt, puts, colored

#summaries = getSummaries(passData) #* summaries[0].string 0 thru 9
#urls = getUrls(passData)
#useableUrls = buildUrls(urls) #* useableUrls[0] 0 thru 9
#stats = getStats(passData) #* stats[0].string // 0,1,2 = votes,answers,views 3,4,5 = votes,answers,views etc...

sys.path.insert(0, os.path.abspath('..'))

if __name__ == '__main__':

    #*************************************************************************************************************#
    #* Application Header
    #*************************************************************************************************************#
    f = Figlet(font='slant')
    puts(colored.yellow(f.renderText('STACK-SEARCH')))

    #*************************************************************************************************************#
    #* Search Prompt / User input / data functions
    #*************************************************************************************************************#
    search = prompt.query("What would you like to search for?: ")
    passData = getSearch(search)
    headings = getHeadings(passData)
    stats = getStats(passData)
    summaries = getSummaries(passData)

    #*************************************************************************************************************#
    #* Question / Header selection
    #*************************************************************************************************************#
    question_options = [
                    {'selector':'1','prompt': colored.cyan(headings[0].text) + 'Votes: ' + colored.yellow(stats[0].string) + ' Answers: ' + colored.yellow(stats[1].string) + ' Views: ' + colored.yellow(stats[2].string),'return':'0'},
                    {'selector':'2','prompt': colored.cyan(headings[1].text) + 'Votes: ' + colored.yellow(stats[3].string) + ' Answers: ' + colored.yellow(stats[4].string) + ' Views: ' + colored.yellow(stats[5].string),'return':'1'},
                    {'selector':'3','prompt': colored.cyan(headings[2].text) + 'Votes: ' + colored.yellow(stats[6].string) + ' Answers: ' + colored.yellow(stats[7].string) + ' Views: ' + colored.yellow(stats[8].string),'return':'2'},
                    {'selector':'4','prompt': colored.cyan(headings[3].text) + 'Votes: ' + colored.yellow(stats[9].string) + ' Answers: ' + colored.yellow(stats[10].string) + ' Views: ' + colored.yellow(stats[11].string),'return':'3'},
                    {'selector':'5','prompt': colored.cyan(headings[4].text) + 'Votes: ' + colored.yellow(stats[12].string) + ' Answers: ' + colored.yellow(stats[13].string) + ' Views: ' + colored.yellow(stats[14].string),'return':'4'},
                    {'selector':'6','prompt': colored.cyan(headings[5].text) + 'Votes: ' + colored.yellow(stats[15].string) + ' Answers: ' + colored.yellow(stats[16].string) + ' Views: ' + colored.yellow(stats[17].string),'return':'5'},
                    {'selector':'7','prompt': colored.cyan(headings[6].text) + 'Votes: ' + colored.yellow(stats[18].string) + ' Answers: ' + colored.yellow(stats[19].string) + ' Views: ' + colored.yellow(stats[20].string),'return':'6'},
                    {'selector':'8','prompt': colored.cyan(headings[7].text) + 'Votes: ' + colored.yellow(stats[21].string) + ' Answers: ' + colored.yellow(stats[22].string) + ' Views: ' + colored.yellow(stats[23].string),'return':'7'},
                    {'selector':'9','prompt': colored.cyan(headings[8].text) + 'Votes: ' + colored.yellow(stats[24].string) + ' Answers: ' + colored.yellow(stats[25].string) + ' Views: ' + colored.yellow(stats[26].string),'return':'8'},
                    {'selector':'10','prompt': colored.cyan(headings[9].text) + 'Votes: ' + colored.yellow(stats[27].string) + ' Answers: ' + colored.yellow(stats[28].string) + ' Views: ' + colored.yellow(stats[29].string),'return':'9'},]
    
    question_selection = prompt.options("Select one of the questions!", question_options)

    #*************************************************************************************************************#
    #* Question Selected Display
    #*************************************************************************************************************#
    puts(colored.magenta('You selected a valid question'.format(question_selection)))

    if question_selection == '0':
        puts(colored.cyan(headings[0].text))
        puts('Votes: ' + colored.yellow(stats[0].string) + ' Answers: ' + colored.yellow(stats[1].string) + ' Views: ' + colored.yellow(stats[2].string))
        puts('Summary: ' + colored.cyan(summaries[0].string))

    elif question_selection == '1':
        puts(colored.cyan(headings[1].text))
        puts('Votes: ' + colored.yellow(stats[3].string) + ' Answers: ' + colored.yellow(stats[4].string) + ' Views: ' + colored.yellow(stats[5].string))
        puts(colored.cyan(summaries[1].string))
    else:
        puts('you failed')


    