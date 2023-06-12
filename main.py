#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Nick Schneider"
__version__ = "0.1.0"
__license__ = "Apache"

import requests
from bs4 import BeautifulSoup


def check_angels_score():
    # url = 'https://www.baseball-reference.com/teams/LAA/2023-schedule-scores.shtml#all_results'
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'html.parser')
    soup = BeautifulSoup(open('angels_scores.html'), features="html.parser")

    # The scores are duplicated on the page so in order to prevent duplicated work we have to narrow our search down to just the main content, not the banner
    table = soup.find(id='team_schedule').tbody
    rows = table.find_all('tr')

    game_num = 0
    for row in rows:
        # Skip the header rows
        if row.get('class'):
            continue

        if game_num > 0:
            previous_game = {
                'game_num': game_num,
                'home_or_visitor': home_or_visitor,
                'runs_scored': runs_scored
            }

        game_num += 1

        fields = row.find_all('td')
        for field in fields:
            if field['data-stat'] == 'boxscore':
                val = field.string
                if val == 'preview':
                    gameHappened = False
                else:
                    gameHappened = True

            if (field['data-stat'] == 'homeORvis'):
                val = field.string
                if val == '@':
                    home_or_visitor = 'away'
                else:
                    home_or_visitor = 'home'

            if (field['data-stat'] == 'R'):
                runs_scored = int(field.string)

        if not gameHappened:
            print(previous_game)
            if previous_game['home_or_visitor'] == 'home' and previous_game['runs_scored'] >= 7:
                return True
            else:
                return False


def main():
    """ Main entry point of the app """

    # TODO: Update to send an email/SMS/notification if this is true
    print("Is Free Chick Fil A Sandwich?:", check_angels_score())


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
