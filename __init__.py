import os
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from s3interface import *

print('Running Script...')

#Starting URL
start_url = "https://www.tesco.ie/groceries/product/browse/default.aspx?N=4294954026&Ne=4294954028"

#list in global scope
tidy_prices = []

# chrome session
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1280x1696')
chrome_options.add_argument('--user-data-dir=/tmp/user-data')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--enable-logging')
chrome_options.add_argument('--log-level=0')
chrome_options.add_argument('--v=99')
chrome_options.add_argument('--single-process')
chrome_options.add_argument('--data-path=/tmp/data-path')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--homedir=/tmp')
chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
#chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"
""" ^ line tells Lambda where to find the headless Chrome binary file"""

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get(start_url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

def scrape_page():
    """Scrapes each page individually, cleans and adds data to list"""
    product_prices = soup.find_all("span", class_="linePrice")
    for price in product_prices:
        tidy_prices.append(price.get_text())

def scraper():
    """Initiates scraper, iterates over 9 pages"""
    scrape_page()
    for pages in range(5):
        scrape_page()
        next_button = driver.find_element_by_link_text("next")
        next_button.click()
    driver.quit()

#Call scraper
scraper()
putS3(tidy_prices)

print('End Script...')

