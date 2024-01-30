from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time


def initialize_yearly_player_data(years):
    base_url = \
        'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'
    for year in years:
        file_path = 'scraping_tools/yearly_player_data/{}.html'.format(year)
        try:  # Create a new file, if it already exists, raise a FileExistsError
            with open(file_path, 'x', encoding='utf-8') as f:
                url = base_url.format(year)
                player_table_html = extract_yearly_player_table(url)
                f.write(str(player_table_html))
        except FileExistsError:
            # If the file already exists, we can simply continue
            continue


def extract_yearly_player_table(url):
    """
    Initiates chrome instnances with selenium to obtain the full HTML table,
    parses this HTML with BeautifulSoup and returns a cleaned version
    :param url: the url we want to scrape data from
    :return:
    """
    chrome_driver_path = "C:/Users/bmurr/Downloads/PersonalProjects/NBA_MVP_Predictor/venv/Lib/site-packages/seleniumbase/drivers/chromedriver.exe"
    # Create a service to start and manage the chrome driver server
    service = Service(chrome_driver_path)
    # Create a driver to control our browser
    driver = webdriver.Chrome(service=service)

    driver.get(url=url)  # Render our URL in our chrome browser
    # Scroll all the way down so that the full table renders
    # Run the JS in the browser to render full table
    driver.execute_script("window.scroll(1,10000")
    time.sleep(2)  # Give the browser appropriate time to exec the script

    html = driver.page_source  # Get the fully rendered HTML
    return parse_html(html)


def parse_html(html):
    """
    Extracts the player stats table from the given HTML page. Strips the web
    page of unnecessary info, returning the relevant mvp table for the page.
    :param page: HTML content of the web page.
    :return: BeautifulSoup object containing the player table.
    """
    soup = BeautifulSoup(html, 'html.parser')
    # Remove redundant rows that repeat row 0 (the list of cols)
    soup.find('tr', class_='thead').decompose()
    # Extract the specific table containing the table with per game stats for
    # each player for the given year
    player_table = soup.find(id='per_game_stats')
    return player_table
