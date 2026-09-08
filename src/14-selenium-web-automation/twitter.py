# Same Twitter search flow, but scrolling the page to load more tweets instead of liking them.
# This is where I first ran into an infinite-scroll page and had to detect "no more new content"
# by comparing document height before and after scrolling.
#
# This is a simplified sibling of twitter-test.py in this same folder: same
# login + search + infinite-scroll pattern, but this version only COLLECTS
# tweet text (no liking) and saves it to a file. See twitter-test.py for a
# more detailed explanation of each Selenium call used below - this file
# focuses its comments on what's different or worth calling out here.
#
# NOTE: like twitter-test.py, this automates the real twitter.com login and
# timeline using hardcoded XPath selectors tied to Twitter's page structure
# at the time this was written. Twitter/X has changed significantly since
# then (including its domain and login flow), so this script is very likely
# to need updating - or may not run at all - against the current site.
from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username, password):
        # Force English UI text so fixed selectors/text checks behave
        # predictably regardless of the browser's own locale.
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def singIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        # Absolute XPaths locating the login form's username/password
        # inputs and submit button - see twitter-test.py for why this style
        # of selector is fragile.
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
        time.sleep(2)
        # Keys.ENTER simulates pressing Enter, submitting the search.
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        results = []

        # renamed from "list" - that was shadowing the builtin, took me a while to notice
        # ("list" is the name of Python's built-in list type/constructor;
        # naming a variable "list" doesn't cause an error, but it hides
        # access to the real list() builtin for the rest of that scope,
        # which can cause confusing bugs later if you try to use list()
        # normally - renaming to tweet_elements avoids that trap.)
        tweet_elements = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]")
        time.sleep(2)
        print("count: "+ str(len(tweet_elements)))

        for i in tweet_elements:
            results.append(i.text)

        loopCounter = 0
        # Reading the page's total scrollable height via JavaScript, so we
        # can tell later whether scrolling actually revealed new content.
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 5:
                # Safety cap: never scroll more than 6 times, even if the
                # page keeps appearing to grow.
                break
            # Scroll to the current bottom of the page, which triggers
            # Twitter to load more tweets via infinite scroll.
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                # Page didn't grow after scrolling - no new tweets loaded,
                # so we've reached the end of what's available.
                break
            last_height = new_height
            loopCounter+=1

            tweet_elements = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]")
            time.sleep(2)
            print("count: "+ str(len(tweet_elements)))

            for i in tweet_elements:
                results.append(i.text)

        count = 1
        # Save every collected tweet's text to a local file, one numbered
        # line per tweet.
        with open("tweets.txt","w",encoding="UTF-8") as file:
            for item in results:
                file.write(f"{count}-{item}\n")
                count+=1


        # count = 1
        # for item in results:
        #     print(f"{count}-{item}")
        #     count+=1
        #     print("***********")



twitter = Twitter(username,password)
# login
twitter.singIn()
twitter.search("python")






