import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from time import sleep

# Load environment variables from .env file
load_dotenv(override=True)

# Get the path to the ChromeDriver from the .env file
chrome_driver_path = os.getenv('CHROME_DRIVER_PATH')

# Set up Chrome options
chrome_options = Options()
# Remove the headless argument to run the browser visibly
# chrome_options.add_argument("--headless")  # Comment out this line

# Set up the Chrome driver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
print("Chrome driver is set up.")
# URL to scrape
url = "https://newyork.craigslist.org/search/astoria-ny/apa#search=2~gallery~81"

# Open the URL
driver.get(url)

# Wait for the page to load
sleep(15)

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
divs = soup.find_all('div', class_='cl-search-result cl-search-view-mode-gallery')
for d in divs:
    link = d.find('a', class_='result-title hdrlnk')
    print(link.text)
    print(link['href'])
    print("=====================================")
# Close the driver
driver.quit()