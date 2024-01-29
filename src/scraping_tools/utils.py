import time
import requests


def make_request(url):
    """
    Make a GET request to the given URL with retries.

    :param url: The URL to send the GET request to.
    :return: Response object if successful.
    :raises InvalidURL: If the URL is unknown.
    :raises TooManyRedirects: If max retries are reached due to too many
    redirects.
    :raises RequestException: For unknown request errors.
    """
    retry_count = 3
    # Send a GET request to the URL
    while retry_count > 0:
        response = requests.get(url)
        if response.status_code in (400, 404):  # Indicates a bad request
            raise requests.exceptions.InvalidURL(f'{url} is an unknown URL')
        elif response.status_code == 429:  # Indicates too many requests
            retry_count -= 1
            # Sleep for 10 seconds before making a new request
            time.sleep(10)
        elif response.status_code != 200:  # Indicates some unknown error
            raise requests.exceptions.RequestException(
                f'Error with status code {response.status_code}encountered')
        else:  # If we are here, we made a successful request
            return response

    # If we are here, we ran out of retries
    raise requests.exceptions.TooManyRedirects(
        f'Reached maximum retries for url {url}.')


def scrape_basketball_reference(years):
    """
    Scrapes MVP, player, and team data from basketball-reference.com and
    saves it into HTML files.

    :param years: List of years for which MVP data is to be scraped.
    :return: None
    """
    # initialize_yearly_mvp_data(years)
    # initialize_yearly_player_data(years)
    # initialize_yearly_team_data(years)
    pass
