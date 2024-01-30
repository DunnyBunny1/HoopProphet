import requests
from bs4 import BeautifulSoup
from utils import make_http_req


def initialize_yearly_mvp_data(years):
    """
    Downloads MVP for each given year and saves each into HTML files
    Iterates through the list of years provided, scrapes the
    web page from the corresponding URL for that year, extracts the relevant
    table data from the page's HTML, and saves the mvp table data into HTML
    files in the corresponding folder.
    If the file for a particular year already exists, skips that year's data.
    :param years: List of years for which MVP data is to be downloaded.
    :raises RuntimeError: If encountering exceptions during URL request.
    """
    # Iterate through each year that we want to scrape data for
    # Iterate through each type of data that we want to scrape data for:
    # MVP data, player data, team data
    url_template = 'https://www.basketball-reference.com/awards/awards_{}.html'
    for year in years:
        file_path = 'scraping_tools/yearly_mvp_data/{}.html'.format(year)
        try:
            # Create a new file, if it already exists, raise a FileExistsError
            with open(file_path, 'x', encoding='utf-8') as f:
                url = url_template.format(year)
                # Try to make a GET request to the URL
                try:
                    response = make_http_req(url)
                except (requests.exceptions.TooManyRedirects,
                        requests.exceptions.RequestException,
                        requests.exceptions.InvalidURL) as e:
                    raise RuntimeError(
                        f'Encountered {e} when making a URL request')
                # Save the html table into a file in our yearly_mvp_data folder
                mvp_table_html = extract_yearly_mvp_table(response.text)
                # Write a string repr. of the page's HTML for the mvp table
                f.write(str(mvp_table_html))
        except FileExistsError:
            # If the file already exists, we can simply continue
            continue


def extract_yearly_mvp_table(page):
    """
    Extracts the MVP table from the given HTML page. Strips the web page of
    unnecessary information, return the relevant mvp table for the page.
    :param page: HTML content of the web page.
    :return: BeautifulSoup object containing the MVP table.
    """
    soup = BeautifulSoup(page, 'html.parser')
    # Remove the 0th table row - it contains unnecessary info for our data
    soup.find('tr', class_='over_header').decompose()
    # Extract the specific table containing MVP voting data
    mvp_table = soup.find(id='mvp')
    return mvp_table
