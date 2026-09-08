# Basics: open a page, take a screenshot, check the title, go back in browser history.
from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2)
# .maximize_window() resizes the browser window to fill the screen - useful
# before a screenshot, so the page renders at a realistic, full-size layout
# instead of whatever small default window size the driver opened with.
driver.maximize_window()
# .save_screenshot(path) captures an image of the current browser viewport
# and writes it to disk as a PNG file at the given path.
driver.save_screenshot("github.com-homepage.png")

url = "http://github.com/octocat"
driver.get(url)

# .title reads the current page's <title> tag content - the text shown in
# the browser tab.
print(driver.title)

if "octocat" in driver.title:
    driver.save_screenshot("github-octocat.png")

time.sleep(2)

# .back() navigates the browser backward in its history, equivalent to
# clicking the browser's back button - here, back to the github.com homepage.
driver.back()
# driver.forward()
# .forward() would be the reverse: move ahead in history again, equivalent
# to clicking the browser's forward button.

time.sleep(2)

# .close() closes the current browser window/tab (as opposed to .quit(),
# which would also end the whole browser session/driver process).
driver.close()
