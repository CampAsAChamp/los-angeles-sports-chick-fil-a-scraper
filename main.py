#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Nick Schneider"
__version__ = "0.1.0"
__license__ = "Apache"

import requests
from bs4 import BeautifulSoup


def get_all_scores():
    # url = 'https://www.baseball-reference.com/boxes/'
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'html.parser')
    soup = BeautifulSoup(open('all_scores.html'), features="html.parser")

    # The scores are duplicated on the page so in order to prevent duplicated work we have to narrow our search down to just the main content, not the banner
    main = soup.find('div', id='content')

    winners = main.find_all('tr', class_='winner')
    losers = main.find_all('tr', class_='loser')
    all_teams = winners + losers

    return check_all_scores(all_teams)


def check_all_scores(results_set):
    for r in results_set:
        tds = r.find_all('td')
        team_name = tds[0].string
        score = int(tds[1].string)
        # Need to add Home vs Away check
        if team_name == 'Los Angeles Angels' and score >= 7:
            return True

    return False


# Improvements: Instead of starting from the first game and going down,
# skip all the way to the bottom and just use the previous game using prev selectors from BS4
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

    is_free_chick_fil_a = check_angels_score()
    # is_free_chick_fil_a = get_all_scores()
    print("Is Free Chick Fil A:", is_free_chick_fil_a)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
