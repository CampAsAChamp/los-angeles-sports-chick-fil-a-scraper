import bs4
import requests

# Fetch the page
url = f'https://www.baseball-reference.com/teams/LAA/{CURRENT_DATETIME.year}-schedule-scores.shtml#all_results'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# Get the table with the games
table = soup.find(id='team_schedule').tbody
rows = table.find_all('tr')

for row in rows:
    # Get all the fields/columns for that row
    fields = row.find_all('td')
    for field in fields:

        # Check if the game has happened or not
        if field['data-stat'] == 'boxscore':
            game_happened = False if field.string == 'preview' else True

        # Check if it was a Home or Away game
        if (field['data-stat'] == 'homeORvis'):
            home_or_away = 'away' if field.string == '@' else 'home'

        # Check to see how many runs they scored
        if (field['data-stat'] == 'R'):
            runs_scored = int(field.string)

if game_happened and home_or_away == 'home' and runs_scored >= 7:
    send_emails()
