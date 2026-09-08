# Twitter automation with a "like while scrolling" step added on top of the search.
# Wrapping the like click in try/except here because a tweet can disappear mid-scroll.
#
# Like the GitHub and Instagram scripts in this folder, this drives a real
# Chrome browser with Selenium to log in, search, and interact with content
# that only loads as you scroll (an "infinite scroll" feed).
#
# NOTE: this automates the real twitter.com login form and timeline using
# hardcoded XPath selectors tied to Twitter's page structure at the time
# this was written. Twitter/X has since changed its site significantly
# (including its domain and login flow), so this script is very likely to
# need updating - or may not run at all - against the current site.
from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username, password):
        # Force English UI text so that the fixed XPath/text checks in this
        # script (like looking for a specific button) behave predictably,
        # regardless of the browser's own locale settings.
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def singIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        # Absolute, position-based XPaths locating the login form's
        # username/password inputs and submit button - fragile the same way
        # as the similar long paths in github.py/instagram.py: they depend
        # on the exact nesting of Twitter's markup at the time this was written.
        usernameInput = self.browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        btnSubmit = self.browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
        btnSubmit.click()

        time.sleep(2)

    def search(self, hashtag):
        searchInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        searchInput.send_keys(hashtag)
        time.sleep(3)
        # Keys.ENTER simulates pressing Enter, submitting the search exactly
        # as a user would.
        searchInput.send_keys(Keys.ENTER)
        time.sleep(3)

        results = []

        # implicitly_wait(seconds) tells Selenium: "whenever I ask to find
        # an element and it isn't there yet, keep retrying for up to this
        # many seconds before giving up" - unlike time.sleep(), which always
        # waits the full duration regardless of whether the page is ready
        # sooner. This is Selenium's built-in "implicit wait" mechanism.
        self.browser.implicitly_wait(5)

        # An XPath using [@data-testid='tweet'] finds elements by a custom
        # "data-testid" attribute - a common pattern in modern web apps
        # where developers tag elements specifically to make them easy for
        # tests/automation to find reliably, rather than relying on CSS
        # classes that might change with styling updates. The
        # "/div[2]/div[2]" part then drills two levels down inside each
        # matched tweet element to reach its text content specifically.
        for i in self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]"):
            results.append(i.text)
            self.like(i)

        time.sleep(3)

        loopCounter = 0
        # execute_script(js_code) runs raw JavaScript inside the browser
        # page and returns its result to Python - here, reading
        # document.documentElement.scrollHeight, i.e. the total scrollable
        # height of the page. Comparing this value before and after
        # scrolling is how the loop below detects "we've reached the bottom
        # and no new content is loading anymore".
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 5:
                # Safety cap: stop after at most 6 scroll attempts even if
                # the page keeps reporting a changing height, to avoid an
                # unbounded loop.
                break
            # Scrolls the browser window all the way to the current bottom
            # of the page, which triggers Twitter's infinite-scroll to load
            # more tweets.
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(3)

            for i in self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]"):
                results.append(i.text)
                self.like(i)

            self.browser.implicitly_wait(5)

            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                # The page didn't get any taller after scrolling and
                # waiting - no new tweets loaded, so we've reached the end
                # of what's available and can stop.
                break
            last_height = new_height
            loopCounter+=1

        count = 1
        # Writes every collected tweet's text to a local file, one numbered
        # line per tweet, so the results can be reviewed without re-running
        # the whole scrape.
        with open("tweets.txt","w",encoding="UTF-8") as file:
            for item in results:
                file.write(f"{count}-{item}\n")
                count+=1

    def like(self, item):
        time.sleep(2)
        # A tweet found earlier in the scroll can disappear from the DOM
        # entirely (Twitter unloads off-screen content to save memory) by
        # the time we try to click its like button - which would make
        # find_element_by_xpath raise an exception. try/except here simply
        # skips that particular like attempt instead of crashing the whole
        # script over one missed tweet.
        try:
            item.find_element_by_xpath("//div[@data-testid='like']").click()
            print("clicked")
        except:
            print("something went wrong")

twitter = Twitter(username,password)
# login
twitter.singIn()
twitter.search("reactjs")




