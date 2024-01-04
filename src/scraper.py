import requests
from bs4 import BeautifulSoup


def scrape_basketball_reference():
    url = 'https://www.basketball-reference.com/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Add your scraping logic here
        # Example: Extracting data from the webpage
        # data = soup.find('div', class_='your-class').text
        return "Scraping Successful"  # Return scraped data or any message
    else:
        return "Failed to fetch data"
