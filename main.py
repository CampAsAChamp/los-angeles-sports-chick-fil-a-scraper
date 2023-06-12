#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Nick Schneider"
__version__ = "0.1.0"
__license__ = "Apache"

import os
import requests
from bs4 import BeautifulSoup
from PyMessenger import Email, SMS, Messenger

# Global Variables
FROM_EMAIL = os.environ['FROM_EMAIL']
TO_EMAIL = os.environ['TO_EMAIL']
PASSWORD = os.environ['PASSWORD']


def check_angels_score():
    url = 'https://www.baseball-reference.com/teams/LAA/2023-schedule-scores.shtml#all_results'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # soup = BeautifulSoup(open('sample_pages/angels_scores.html'), features="html.parser")

    # The scores are duplicated on the page so in order to prevent duplicated work we have to narrow our search down to just the main content, not the banner
    table = soup.find(id='team_schedule').tbody
    rows = table.find_all('tr')

    game_num = 0
    for row in rows:
        # Skip the header rows
        if row.get('class') and 'thead' in row['class']:
            continue

        if game_num > 0:
            previous_game = {
                'game_num': game_num,
                'home_or_away': home_or_away,
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
                    home_or_away = 'away'
                else:
                    home_or_away = 'home'

            if (field['data-stat'] == 'R'):
                runs_scored = int(field.string)

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

    if check_angels_score():
        send_email()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
