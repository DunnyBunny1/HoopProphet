import time

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.basketball-reference.com/awards/awards_{}.html'
"""
years: A list of years (integers) for which MVP data needs to be 
    scraped.
"""
years = [year for year in range(1991, 2023)]


def make_request(url):
    """
    Make a GET request to the given URL with retries.

    :param url: The URL to send the GET request to.
    :return: Response object if successful.
    :raises  requests.exceptions.InvalidURL: If the URL is unknown.
    :raises requests.exceptions.TooManyRedirects: If max retries are reached.
    :raises requests.exceptions.RequestException: For unknown request errors.
    """
    retry_count = 3
    # Send a GET request to the URL
    while retry_count > 0:
        response = requests.get(url)
        if response.status_code == 400:  # Indicates a bad request
            raise requests.exceptions.InvalidURL(f'{url} is an unknown URL')
        elif response.status_code == 429:  # Indicates too many requests
            retry_count -= 1
            # Sleep for 10 seconds before making a new request
            time.sleep(10)
        elif response.status_code != 200:  # Indicates some unknown error
            raise requests.exceptions.RequestException('Unknown error with '
                                                       f'status code {response.status_code} encountered')
        else:  # If we are here, we made a successful request
            return response

    # If we are here, we ran out of retries
    raise requests.exceptions.TooManyRedirects(
        f'Reached maximum retries for url {url}.')


def initialize_yearly_mvp_data():
    """
    Scrapes MVP data for each given year and saves it into HTML files

    This function iterates through the list of years provided, scrapes MVP
    data from the corresponding URLs, and saves the data into HTML files in
    the 'yearly_mvp_data' folder.
    If the file for a particular year already exists, it skips that year's data.

    Example:
    >>> yrs = [2018, 2019, 2020]
    >>> initialize_yearly_mvp_data(years)
    """
    # Iterate through each year that we want to scrape MVP data for
    for year in years:
        file_path = 'src/yearly_mvp_data/{}.html'.format(year)
        try:
            with open(file_path, 'x', encoding='utf-8') as f:
                # If we successfully created the file, write our html to it
                # Get the url corresponding to the current year
                url = base_url.format(year)
                # Try to make a GET request to the URL
                try:
                    response = make_request(url)
                except (requests.exceptions.TooManyRedirects,
                        requests.exceptions.RequestException,
                        requests.exceptions.InvalidURL) as e:
                    raise RuntimeError(
                        f'Encountered {e} when making a URL request')
                # Save the web page into a file in our yearly_mvp_data folder
                # Create the file with our new data
                f.write(response.text)
        except FileExistsError:
            # If the file already exists, we can simply continue
            pass


def get_yearly_mvp_voting_tables():
    """
    Returns a mapping of years to the mvp voting table html from that year

    :return: a dictionary of year (str) : voting table (str)
    """
    # Initialize a dict to hold mvp voting tables
    mvp_voting_tables = {}
    for year in years:
        file_path = 'src/yearly_mvp_data/{}.html'.format(year)
        with open(file_path, 'r', encoding='utf-8') as f:
            page = f.read()
            soup = BeautifulSoup(page, 'html.parser')
            # Remove the 0th table row - it contains unnecessary info for our
            # data
            soup.find('tr', class_='over_header').decompose()
            # Extract the specific table containing MVP voting data
            mvp_table = soup.find(id='mvp')
            mvp_voting_tables[str(year)] = mvp_table
    return mvp_voting_tables


def scrape_basketball_reference():
    """
    Scrapes basketball reference MVP data and returns voting tables.

    :return: A dictionary of year (str) : voting table (str)
    """
    initialize_yearly_mvp_data()
    return get_yearly_mvp_voting_tables()
