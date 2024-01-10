import time

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.basketball-reference.com/awards/awards_{}.html'


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


def initialize_yearly_mvp_data(years):
    """
    Downlaods MVP data for each given year and saves it into HTML files

    Iterates through the list of years provided, scrapes the
    web page from the corresponding URL for that year, extracts the relevant
    mvp table data from the page's HTML, and saves the mvp table data into HTML
    files in the'yearly_mvp_data' folder.
    If the file for a particular year already exists, it skips that year's data.

    :param years: List of years for which MVP data is to be downloaded.
    :return: None
    :raises RuntimeError: If encountering exceptions during URL request.

    Example:
    ```
    yrs = [2018, 2019, 2020]
    initialize_yearly_mvp_data(yrs)
    ```
    After running the function, HTML files for each year (2018.html, 2019.html,
    2020.html) will be created in the 'yearly_mvp_data' folder.
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
                # Strip the web page of unnecessary information, return the
                # relevant mvp table for the given year
                # Save the html table into a file in our yearly_mvp_data folder
                # Create the file with our new data
                mvp_table_html = extract_table_from_page(year, response.text)
                # Write a human-readable, string representation of the page's
                # HTML for the mvp table
                f.write(mvp_table_html.prettify())
        except FileExistsError:
            # If the file already exists, we can simply continue
            continue


def extract_table_from_page(year, page):
    """
    Extracts the MVP table from the HTML page for a given year.

    :param year: The year for which the MVP table is being extracted.
    :param page: HTML content of the web page.
    :return: BeautifulSoup object containing the MVP table.
    """
    soup = BeautifulSoup(page, 'html.parser')
    # Remove the 0th table row - it contains unnecessary info for our data
    soup.find('tr', class_='over_header').decompose()
    # Extract the specific table containing MVP voting data
    mvp_table = soup.find(id='mvp')
    return mvp_table


def scrape_basketball_reference(years):
    """
    Scrapes MVP data from basketball-reference.com and saves it into HTML files.

    This function initializes the process of scraping MVP data by calling
    'initialize_yearly_mvp_data()' function.

    :param years: List of years for which MVP data is to be scraped.
    :return: None
    """
    initialize_yearly_mvp_data(years)
