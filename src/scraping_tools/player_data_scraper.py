from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def initialize_yearly_player_data(years):
    base_url = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'
    for year in years:
        file_path = 'scraping_tools/yearly_player_data/{}.html'.format(year)
        try:
            with open(file_path, 'x', encoding='utf-8') as f:
                url = base_url.format(year)
                player_table_html = extract_yearly_player_table(year, url)
                f.write(str(player_table_html))
        except FileExistsError:
            # If the file already exists, we can simply continue
            continue


def extract_yearly_player_table(year, url):
    """
    Use selenium to obtain the full HTML table, parse w/ bs4
    :param year:
    :param url:
    :return:
    """
    chrome_driver_path = "C:/Users/bmurr/Downloads/PersonalProjects/NBA_MVP_Predictor/venv/Lib/site-packages/seleniumbase/drivers/chromedriver.exe"
    file_path = 'src/yearly_player_data/{}.html'.format(year)
    # Create a service to start and manage the chrome driver server
    service = Service(chrome_driver_path)
    # Create a driver to control our browser
    driver = webdriver.Chrome(service=service)
    # Render our URL in our chrome browser
    driver.get(url=url)
    # Run the JS in the browser to render full table
    # Scroll all the way down to the full table renders
    driver.execute_script("window.scroll(1,10000")
    # Give the browser appropraite time to exec the script
    time.sleep(2)
    html = driver.page_source  # Get the fully rendered HTML
    return parse_html(html)


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Remove the 0th table row - it contains unnecessary info for our data
    soup.find('tr', class_='over_header').decompose()
    # Extract the specific table containing MVP voting data
    mvp_table = soup.find(id='mvp')
    return mvp_table