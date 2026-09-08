# First check that the webdriver install actually works: open a browser and load a page.
#
# Selenium itself is just a Python library - to actually control a real
# browser it needs a matching "driver" executable that acts as a bridge
# between your Python code and the browser (chromedriver.exe for Chrome,
# geckodriver.exe for Firefox - both included alongside these scripts in
# this folder). This script is the simplest possible smoke test: launch a
# browser and load one page, to confirm the driver is installed and working
# before writing anything more complex.
from selenium import webdriver

# driver = webdriver.Chrome()
# webdriver.Firefox() launches a real Firefox window controlled by Selenium,
# using geckodriver.exe (Firefox's equivalent of chromedriver) behind the
# scenes.
driver = webdriver.Firefox()

url = "https://example.com"

# .get(url) tells the already-open browser to navigate to this address -
# exactly like typing it into the address bar and pressing Enter. If this
# runs without errors and a browser window pops up showing example.com,
# the Selenium + geckodriver setup is working correctly.
driver.get(url)
