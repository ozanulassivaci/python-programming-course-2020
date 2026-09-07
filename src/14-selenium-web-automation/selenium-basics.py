# Basics: open a page, take a screenshot, check the title, go back in browser history.
from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")

url = "http://github.com/octocat"
driver.get(url)

print(driver.title)

if "octocat" in driver.title:
    driver.save_screenshot("github-octocat.png")

time.sleep(2)

driver.back()
# driver.forward()

time.sleep(2)

driver.close()

