#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Nick Schneider"
__version__ = "0.1.0"
__license__ = "Apache"

import datetime
import os
import requests
from bs4 import BeautifulSoup
from PyMessenger import Email, SMS, Messenger

# Global Variables
FROM_EMAIL = os.environ['FROM_EMAIL']
TO_EMAIL = os.environ['TO_EMAIL']
PASSWORD = os.environ['PASSWORD']


def check_angels_score():
    current_year = datetime.datetime.now().year
    url = f'https://www.baseball-reference.com/teams/LAA/{current_year}-schedule-scores.shtml#all_results'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # soup = BeautifulSoup(open('sample_pages/angels_scores.html'), features="html.parser")

    # The scores are duplicated on the page (once in the banner and once on the main page)
    # so in order to prevent duplicated work we have to narrow our search down to just the main content (table body or tbody), and not include the banner
    table = soup.find(id='team_schedule').tbody
    rows = table.find_all('tr')

    # Search for the last played game by checking each row to see if that row/game has been played or not
    # If it hasn't it will say preview in the main box and that is our trigger to know we need to stop
    game_num = 1
    for row in rows:
        # Skip the header rows which have the class='thead'
        if row.get('class') and 'thead' in row['class']:
            continue

        # Keep track of the previous game because once we find a game that hasn't been played yet we know the previous one we just checked is the last played game
        if game_num > 1:
            previous_game = {
                'game_num': game_num,
                'home_or_away': home_or_away,
                'runs_scored': runs_scored
            }

        # Each row has multiple <td> columns with the different stats (Date, Opponent, Runs Scored, Runs Allowed, etc...)
        # Search through all those fields and extract the columns that we want, parsing the data to be easiest to work with
        #     - Played Yet?
        #     - Home or Away
        #     - Runs Scored
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
                    home_or_away = 'away'
                else:
                    home_or_away = 'home'

            if (field['data-stat'] == 'R'):
                runs_scored = int(field.string)

        game_num += 1

        if not gameHappened:
            print(previous_game)

            if previous_game['home_or_away'] == 'home' and previous_game['runs_scored'] >= 7:
                return True
            else:
                return False


def send_email():
    messenger = Messenger(FROM_EMAIL, PASSWORD)

    # Build the message
    subject = 'Angels Chick Fil A Reminder'
    body = 'Angels won by 7 or more runs!'
    msg = Email(TO_EMAIL, subject, body, is_HTML=False)

    # Send the message
    messenger.send_email(msg, one_time=True)


def main():
    """ Main entry point of the app """
    # If the season is over and every game has been played this will scan through all the games but ultimately won't do anything because there are no future games

    # Only run from March - October
    current_month = datetime.datetime.now().month
    if 3 <= current_month <= 10:
        if check_angels_score():
            send_email()
            print("Email successfully sent!")
        else:
            print("Angels score didn't meet the criteria for free Chick Fil A :^(")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
