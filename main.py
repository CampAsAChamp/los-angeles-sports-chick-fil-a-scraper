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
from PyMessenger import Email, Messenger

# Global Variables
FROM_EMAIL = os.environ['FROM_EMAIL']
TO_EMAIL = os.environ['TO_EMAIL']
PASSWORD = os.environ['PASSWORD']

M_JANUARY = 1
M_FEBRUARY = 2
M_MARCH = 3
M_APRIL = 4
M_MAY = 5
M_JUNE = 6
M_JULY = 7
M_AUGUST = 8
M_SEPTEMBER = 9
M_OCTOBER = 10
M_NOVEMBER = 11
M_DECEMBER = 12


def check_angels_score():
    """ At any home game, if the Angels score 7 or more runs, you can claim a chicken sandwich """

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


def check_lafc_score():
    """ At any home game, if LAFC wins, you can claim a chicken sandwich """

    current_year = datetime.datetime.now().year
    url = f'https://fbref.com/en/squads/81d817a3/{current_year}/matchlogs/c22/schedule/Los-Angeles-FC-Scores-and-Fixtures-Major-League-Soccer'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # soup = BeautifulSoup(
    # open('sample_pages/2023_lafc_scores.html'), features="html.parser")

    # The scores are duplicated on the page (once in the banner and once on the main page)
    # so in order to prevent duplicated work we have to narrow our search down to just the main content (table body or tbody), and not include the banner
    table = soup.find(id='all_matchlogs').tbody
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
                'win_or_loss': win_or_loss
            }

        # Each row has multiple <td> columns with the different stats (Date, Opponent, Runs Scored, Runs Allowed, etc...)
        # Search through all those fields and extract the columns that we want, parsing the data to be easiest to work with
        #     - Played Yet?
        #     - Home or Away?
        #     - Win or Loss?
        fields = row.find_all('td')
        for field in fields:
            if field['data-stat'] == 'result':
                val = field.string
                if val is None:
                    gameHappened = False
                else:
                    gameHappened = True
                    win_or_loss = field.string

            if (field['data-stat'] == 'venue'):
                home_or_away = field.string

        game_num += 1

        if not gameHappened:
            print(previous_game)

            if previous_game['home_or_away'] == 'Home' and previous_game['win_or_loss'] == 'W':
                return True
            else:
                return False


def check_ducks_score():
    """ At any home game, if the Ducks score 5 or more goals, you can claim a chicken sandwich """

    current_year = datetime.datetime.now().year
    url = f'https://www.hockey-reference.com/teams/ANA/{current_year}_games.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # soup = BeautifulSoup(
    # open('sample_pages/2023_ducks_scores.html'), features="html.parser")

    # The scores are duplicated on the page (once in the banner and once on the main page)
    # so in order to prevent duplicated work we have to narrow our search down to just the main content (table body or tbody), and not include the banner
    table = soup.find(id='all_games').tbody
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
                'goals_scored': goals_scored
            }

        # Each row has multiple <td> columns with the different stats (Date, Opponent, Runs Scored, Runs Allowed, etc...)
        # Search through all those fields and extract the columns that we want, parsing the data to be easiest to work with
        #     - Played Yet?
        #     - Home or Away
        #     - Goals Scored
        fields = row.find_all('td')
        for field in fields:
            if field['data-stat'] == 'game_outcome':
                val = field.string
                if val is None:
                    gameHappened = False
                else:
                    gameHappened = True

            if (field['data-stat'] == 'game_location'):
                val = field.string
                if val == '@':
                    home_or_away = 'away'
                else:
                    home_or_away = 'home'

            if (field['data-stat'] == 'goals'):
                goals_scored = int(field.string)

        game_num += 1

        if not gameHappened:
            print(previous_game)

            if previous_game['home_or_away'] == 'home' and previous_game['goals_scored'] >= 5:
                return True
            else:
                return False


def send_email(subject, body):
    messenger = Messenger(FROM_EMAIL, PASSWORD)
    messenger.open_conn()

    emails = TO_EMAIL.split(',')
    for email in emails:
        msg = Email(email, subject, body)
        messenger.send_email(msg)

    messenger.close_conn()


def main():
    """ Main entry point of the app """

    # If the season is over for one of the teams and every game has been played
    # this will scan through all the games but ultimately won't do anything because there are no future games

    current_month = datetime.datetime.now().month

    # Only run from March - October
    if M_MARCH <= current_month <= M_OCTOBER:
        if check_angels_score():
            subject = 'Angels Chick Fil A Reminder'
            body = 'Angels won by 7 or more runs!'
            send_email(subject, body)
            print("✔ - Email successfully sent!")
        else:
            print("✗ - Angels didn't meet the criteria")
    else:
        print("✗ - Angels are not in season")

    print()

    # Only run from October - April
    if current_month >= M_OCTOBER or current_month <= M_JUNE:
        if check_ducks_score():
            subject = 'Ducks Chick Fil A Reminder'
            body = 'Ducks won by 5 or more goals!'
            send_email(subject, body)
            print("✔ - Email successfully sent!")
        else:
            print("✗ - Ducks score didn't meet the criteria")
    else:
        print("✗ - Ducks are not in season")

    print()

    # Always run because LAFC season is basically the whole year
    if check_lafc_score():
        subject = 'LAFC Chick Fil A Reminder'
        body = 'LAFC won at home!'
        send_email(subject, body)
        print("✔ - Email successfully sent!")
    else:
        print("✗ - LAFC didn't meet the criteria")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
