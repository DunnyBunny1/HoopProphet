import time

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.basketball-reference.com/awards/awards_{}.html'
years = [yr for yr in range(1991, 2023)]


def scrape_basketball_reference():
    # TODO: Refactor this to use lazy singleton init
    # initialize_yearly_mvp_data(years)
    return get_yearly_mvp_voting_tables()


def initialize_yearly_mvp_data(years):
    # Iterate through each year that we want to scrape MVP data for
    for year in years:
        # Get the url corresponding to the current year
        url = base_url.format(year)
        # Send a GET request to the URL
        response = requests.get(url)
        if response.status_code == 200:
            # Save the web page into a file in our yearly_mvp_data folder
            # Create the file if it does not already exist
            file_path = './yearly_mvp_data/{}.html'.format(year)
            try:
                with open(file_path, 'x', encoding='utf-8') as f:
                    # If we successfully created the file, write our html to it
                    f.write(response.text)
            except FileExistsError:
                # If the file already exists, we can simply continue
                pass
        elif response.status_code == 429:
            time.sleep(10)


def get_yearly_mvp_voting_tables():
    # Initialize a dict to hold mvp voting tables
    mvp_voting_tables = {}
    for year in years:
        file_path = 'src/yearly_mvp_data/{}.html'.format(year)
        with open(file_path, 'r', encoding='utf-8') as f:
            page = f.read()
            soup = BeautifulSoup(page, 'html.parser')
            # Remove the 0th table row - it contains unnecessary info for our dat
            soup.find('tr', class_='over_header').decompose()
            # Extract the specific table containing MVP voting data
            mvp_table = soup.find(id='mvp')
            mvp_voting_tables[str(year)] = mvp_table
