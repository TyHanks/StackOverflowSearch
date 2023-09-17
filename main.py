import sys
import os
from scripts.data import *
from pyfiglet import Figlet
from clint.textui import prompt, puts, colored

sys.path.insert(0, os.path.abspath(".."))

if __name__ == "__main__":
    # *************************************************************************************************************#
    # * Application Header
    # *************************************************************************************************************#
    f = Figlet(font="slant")
    puts(colored.yellow(f.renderText("STACK-SEARCH")))

    # *************************************************************************************************************#
    # * Search Prompt / User input / data functions
    # *************************************************************************************************************#
    search = prompt.query("What would you like to search for?: ")
    passData = getSearch(search)
    headings = getHeadings(passData)
    stats = getStats(passData)
    summaries = getSummaries(passData)
    # ?: Possible future feature - 1: urls = getUrls(passData)
    # ?: Possible future feature - 1: useableUrls = buildUrls(urls)

    # *************************************************************************************************************#
    # * Question / Header selection
    # *************************************************************************************************************#
    question_options = [
        {
            "selector": "1",
            "prompt": colored.cyan(headings[0].text)
            + "Votes: "
            + colored.yellow(stats[0].string)
            + " Answers: "
            + colored.yellow(stats[1].string)
            + " Views: "
            + colored.yellow(stats[2].string),
            "return": "0",
        },
        {
            "selector": "2",
            "prompt": colored.cyan(headings[1].text)
            + "Votes: "
            + colored.yellow(stats[3].string)
            + " Answers: "
            + colored.yellow(stats[4].string)
            + " Views: "
            + colored.yellow(stats[5].string),
            "return": "1",
        },
        {
            "selector": "3",
            "prompt": colored.cyan(headings[2].text)
            + "Votes: "
            + colored.yellow(stats[6].string)
            + " Answers: "
            + colored.yellow(stats[7].string)
            + " Views: "
            + colored.yellow(stats[8].string),
            "return": "2",
        },
        {
            "selector": "4",
            "prompt": colored.cyan(headings[3].text)
            + "Votes: "
            + colored.yellow(stats[9].string)
            + " Answers: "
            + colored.yellow(stats[10].string)
            + " Views: "
            + colored.yellow(stats[11].string),
            "return": "3",
        },
        {
            "selector": "5",
            "prompt": colored.cyan(headings[4].text)
            + "Votes: "
            + colored.yellow(stats[12].string)
            + " Answers: "
            + colored.yellow(stats[13].string)
            + " Views: "
            + colored.yellow(stats[14].string),
            "return": "4",
        },
        {
            "selector": "6",
            "prompt": colored.cyan(headings[5].text)
            + "Votes: "
            + colored.yellow(stats[15].string)
            + " Answers: "
            + colored.yellow(stats[16].string)
            + " Views: "
            + colored.yellow(stats[17].string),
            "return": "5",
        },
        {
            "selector": "7",
            "prompt": colored.cyan(headings[6].text)
            + "Votes: "
            + colored.yellow(stats[18].string)
            + " Answers: "
            + colored.yellow(stats[19].string)
            + " Views: "
            + colored.yellow(stats[20].string),
            "return": "6",
        },
        {
            "selector": "8",
            "prompt": colored.cyan(headings[7].text)
            + "Votes: "
            + colored.yellow(stats[21].string)
            + " Answers: "
            + colored.yellow(stats[22].string)
            + " Views: "
            + colored.yellow(stats[23].string),
            "return": "7",
        },
        {
            "selector": "9",
            "prompt": colored.cyan(headings[8].text)
            + "Votes: "
            + colored.yellow(stats[24].string)
            + " Answers: "
            + colored.yellow(stats[25].string)
            + " Views: "
            + colored.yellow(stats[26].string),
            "return": "8",
        },
        {
            "selector": "10",
            "prompt": colored.cyan(headings[9].text)
            + "Votes: "
            + colored.yellow(stats[27].string)
            + " Answers: "
            + colored.yellow(stats[28].string)
            + " Views: "
            + colored.yellow(stats[29].string),
            "return": "9",
        },
    ]

    question_selection = prompt.options(
        "Select one of the questions!", question_options
    )

    # *************************************************************************************************************#
    # * Question Selected Display
    # *************************************************************************************************************#
    puts(
        colored.yellow(
            "-----------------------------------------------------------------"
        )
    )

    def choice_prompt():
        choice_options = [
            {"selector": "o", "prompt": "View Answers", "return": "o"},
            {"selector": "s", "prompt": "Search Again", "return": "s"},
            {"selector": "q", "prompt": "Close / Quit", "return": "quit"},
        ]
        choice_selection = prompt.options("Select an option", choice_options)
        return choice_selection

    def choice_prompt_actions(choice_selection, question_number):
        if choice_selection == "o":
            print("")
        elif choice_selection == "s":
            ## Search again
            python = sys.executable
            os.execl(python, python, *sys.argv)
        else:
            ## Close application
            sys.exit(0)

    if question_selection == "0":
        puts(colored.cyan(headings[0].text))
        puts(
            "Votes: "
            + colored.yellow(stats[0].string)
            + " Answers: "
            + colored.yellow(stats[1].string)
            + " Views: "
            + colored.yellow(stats[2].string)
        )
        # ?: Possible future feature - 1: puts(colored.blue(useableUrls[0]))
        puts("Summary: " + colored.cyan(summaries[0].string.lstrip()))
        choice_selection = choice_prompt()
        question_number = 0
        choice_action = choice_prompt_actions(choice_selection, question_number)
    elif question_selection == "1":
        puts(colored.cyan(headings[1].text))
        puts(
            "Votes: "
            + colored.yellow(stats[3].string)
            + " Answers: "
            + colored.yellow(stats[4].string)
            + " Views: "
            + colored.yellow(stats[5].string)
        )
        # ?: Possible future feature - 1: puts(colored.blue(useableUrls[0]))
        puts("Summary: " + colored.cyan(summaries[1].string.lstrip()))
        choice_selection = choice_prompt()
        question_number = 1
        choice_action = choice_prompt_actions(choice_selection, question_number)
        #!: Finish rest of question_selections 2, 3, 4, 5, 6, 7, 8, 9
    else:
        puts("Try selection again")
