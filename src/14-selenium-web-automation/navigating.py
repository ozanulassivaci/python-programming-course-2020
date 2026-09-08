# Typing into a search box and pressing Enter with Selenium, then reading the results back.
#
# This builds on installing.py: not just opening a page, but interacting
# with it (typing text, pressing a key) and then reading data back out of
# the resulting page.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url ="http://github.com"
driver.get(url)


# This XPath is an absolute, position-based path down the page's structure
# to reach GitHub's top search input box - fragile in the same way as the
# similar long XPaths in github.py/instagram.py: a page redesign could
# easily break it, since it doesn't refer to any stable id or class.
searchInput = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
# Keys.ENTER simulates pressing the Enter key on the keyboard, submitting
# the search exactly as a user pressing Enter in that field would.
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
# result = driver.page_source
# .page_source would give the full rendered HTML of the results page as a
# string (handy for feeding into BeautifulSoup, for example), but instead
# this script asks Selenium directly for the matching elements: every <a>
# tag nested inside an <h3> nested inside an element with class
# "repo-list-item" - i.e. the repository name links in the search results.
result = driver.find_elements_by_css_selector(".repo-list-item h3 a")

for element in result:
    print(element.text)

# .close() closes the current browser window/tab that Selenium opened.
driver.close()
