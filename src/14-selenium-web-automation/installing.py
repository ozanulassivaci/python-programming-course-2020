# First check that the webdriver install actually works: open a browser and load a page.
from selenium import webdriver

# driver = webdriver.Chrome()
driver = webdriver.Firefox()

url = "https://example.com"

driver.get(url)

