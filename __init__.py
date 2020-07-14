from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

print('Running Script...')

#urls
start_url = "https://www.tesco.ie/groceries/product/browse/default.aspx?N=4294954026&Ne=4294954028"



# chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())

page = driver.get(start_url)

tidy_prices = []

def scrape_page():
    product_prices = soup.find_all("span", class_="linePrice")

    for price in product_prices:
        tidy_prices.append(price.get_text())

for pages in range(10):
    scrape_page()
    next_button = driver.find_element_by_link_text("next")
    next_button.click()


driver.quit()

print(tidy_prices)

print('End Script...')

