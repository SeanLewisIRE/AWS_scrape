from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

print('Running Script...')

#Starting URL
start_url = "https://www.tesco.ie/groceries/product/browse/default.aspx?N=4294954026&Ne=4294954028"

#list in global scope
tidy_prices = []

# chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())
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
    for pages in range(9):
        scrape_page()
        next_button = driver.find_element_by_link_text("next")
        next_button.click()
    driver.quit()

#Call scraper
scraper()

print(tidy_prices)

print('End Script...')

