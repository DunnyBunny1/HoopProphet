from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
chrome_driver_path = "C:/Users/bmurr/Downloads/PersonalProjects/NBA_MVP_Predictor/venv/Lib/site-packages/seleniumbase/drivers/chromedriver.exe"

# Create a service to start and manage the chrome driver server
service = Service(chrome_driver_path)
# Create a driver to control our browser
driver = webdriver.Chrome(service=service)
# Navigate to this URL
driver.get("https://www.bing.com")
time.sleep(4)
# Close the web browser window when we are done
driver.close()
