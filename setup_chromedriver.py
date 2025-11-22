"""
This script verifies that Selenium and the appropriate ChromeDriver are installed and working
correctly on this machine. It uses `webdriver-manager` to automatically install the correct
ChromeDriver version and opens a Chrome browser to google.com for 4 seconds.
Run this once after setting up the project to ensure your scraping tools are ready.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    # Create a service to start and manage the chrome driver server
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Navigate to google.com to verify the browser works
    driver.get("https://www.google.com")
    time.sleep(4)
    driver.close()


if __name__ == "__main__":
    main()
