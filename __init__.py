from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

print('Running Script...')



url = "https://www.tesco.ie/groceries/product/browse/default.aspx?N=4294954026&Ne=4294954028"

# chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

driver.quit()

product_prices = soup.find_all("span", class_="linePrice")
tidy_prices = []
for price in product_prices:
    tidy_prices.append(price.get_text())

print(tidy_prices)

print('End Script...')
