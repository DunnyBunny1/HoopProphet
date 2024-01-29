import requests
from bs4 import BeautifulSoup
from utils import make_request


def initialize_yearly_mvp_data(years):
    """
    Downloads MVP for each given year and saves each into HTML files

    Iterates through the list of years provided, scrapes the
    web page from the corresponding URL for that year, extracts the relevant
    table data from the page's HTML, and saves the mvp table data into HTML
    files in the corresponding folder.
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
    # Iterate through each year that we want to scrape data for
    # Iterate through each type of data that we want to scrape data for:
    # MVP data, player data, team data
    url_template = 'https://www.basketball-reference.com/awards/awards_{}.html'
    for year in years:
        file_path = 'scraping_tools/yearly_mvp_data/{}.html'.format(year)
        try:
            with open(file_path, 'x', encoding='utf-8') as f:
                # If we successfully created the file, write our html to it
                # Get the url corresponding to the current year
                url = url_template.format(year)
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
                mvp_table_html = extract_yearly_mvp_table(response.text)
                # Write a string repr. of the page's HTML for the mvp table
                f.write(str(mvp_table_html))
        except FileExistsError:
            # If the file already exists, we can simply continue
            continue


def extract_yearly_mvp_table(year, page):
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
