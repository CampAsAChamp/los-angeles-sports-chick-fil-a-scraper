import datetime
import os

import requests
from bs4 import BeautifulSoup

import constants
import globals


def readBoolEnvVar(key: str, default_value: str):
    return os.getenv(key, default_value).lower() in ('true', 't', '1')


def print_criteria_not_met(team_name: str):
    print(f"✗ - {team_name} didn't meet the criteria")


def print_not_in_season(team_name: str):
    print(f"✗ - {team_name} are not in season")


def generate_email_subject(team_name: str) -> str:
    return f"{team_name} Chick Fil A Reminder"


def fetch_soup(url: str) -> BeautifulSoup:
    """ 
    Makes HTTP GET request to the URL and loads it into BS4 for further parsing 
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup


def check_yesterday(game_date: datetime) -> bool:
    """ 
    Checks to see if the day of the game was yesterday 
    """

    return (globals.CURRENT_DATETIME.date() - game_date == datetime.timedelta(days=1))


def color_text(text: str, color: str):
    if color == constants.BLACK:
        color = constants.BLACK_CODE
    elif color == constants.RED:
        color = constants.RED_BLACK_CODE
    elif color == constants.GREEN:
        color = constants.GREEN_BLACK_CODE
    elif color == constants.YELLOW:
        color = constants.YELLOW_BLACK_CODE
    elif color == constants.BLUE:
        color = constants.BLUE_BLACK_CODE
    elif color == constants.MAGENTA:
        color = constants.MAGENTA_BLACK_CODE
    elif color == constants.CYAN:
        color = constants.CYAN_BLACK_CODE
    elif color == constants.WHITE:
        color = constants.WHITE_BLACK_CODE
    else:
        return text

    return color + text + constants.RESET_CODE


def color_print_game(game: dict, color: str):
    for key, val in game.items():
        print(color_text(key, color), ":", val, end=", ")
    print()
