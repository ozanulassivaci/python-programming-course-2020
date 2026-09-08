# Instagram automation: log in, scroll the followers dialog, and follow/unfollow accounts.
# This one taught me that a lot of "scraping" is really just waiting and scrolling.
#
# Like github.py, this drives a real Chrome browser with Selenium instead of
# just downloading raw HTML - necessary here because Instagram's follower
# list is loaded dynamically (more names appear only as you scroll) rather
# than all being present in the page at once.
#
# NOTE: this automates Instagram's real login form and follower dialog using
# hardcoded XPath/CSS selectors. Instagram changes its page structure often
# and actively tries to detect/limit automated browsing, so this script is
# not guaranteed to keep working unmodified, and using it against a real
# account carries a risk of that account being flagged or restricted.
from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self,username,password):
        # ChromeOptions lets you configure the browser before it launches.
        # Here, 'intl.accept_languages' forces Chrome to request English
        # content from Instagram, so the page text/button labels this script
        # looks for (like "Following") come back in a predictable language
        # instead of whatever the browser's default locale would fetch.
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # Passing a path to chromedriver.exe explicitly (instead of relying
        # on it being found via PATH) plus chrome_options=... applies the
        # language settings above to the launched browser instance.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        # These XPath expressions walk down a very specific, exact chain of
        # nested elements to reach the username/password <input> boxes
        # inside Instagram's login form. This kind of "absolute path" XPath
        # is fragile - a small layout change on Instagram's side can break
        # it entirely, since it doesn't refer to any stable id or class name.
        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        # Keys.ENTER simulates pressing the Enter key - here, submitting the
        # login form the same way a user pressing Enter in the password
        # field would.
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self, max):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        # Clicks the "X followers" link on the profile page, which opens a
        # popup dialog listing them.
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        # A CSS selector can combine an attribute selector with a
        # descendant: "div[role=dialog] ul" means "a <ul> that is somewhere
        # inside a <div> whose role attribute equals 'dialog'" - i.e. the
        # list inside the followers popup specifically.
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"first count: {followerCount}")

        # ActionChains lets you build up a sequence of low-level input
        # actions (key presses, mouse moves, clicks...) and then run them
        # together with .perform().
        action = webdriver.ActionChains(self.browser)

        # Instagram only loads more followers into the dialog as you scroll
        # it, so this loop repeatedly "presses" the space bar (a common way
        # to scroll a focused, scrollable element down) and re-counts the
        # <li> items, stopping once we've reached the desired "max" count or
        # once scrolling stops revealing any new followers (newCount doesn't
        # change anymore, meaning we've hit the bottom of the list).
        while followerCount < max:
            dialog.click()  # focus the dialog so the space-bar scroll actually applies to it
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"second count: {newCount}")
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")

        followerList = []
        i = 0
        for user in followers:
            # get_attribute("href") reads the value of an attribute that
            # Selenium doesn't expose as a dedicated property (unlike
            # .text) - here, the profile URL from each follower's <a> link.
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)
            i += 1
            if i == max:
                break

        # Saves the collected follower profile links to a plain text file,
        # one per line, so they can be reused later (e.g. by followUser()
        # below) without having to scrape them again.
        with open("followers.txt", "w",encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")

    def followUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        # find_element_by_tag_name grabs the FIRST <button> on the page -
        # on a profile page that's the Follow/Following button, and its
        # .text tells us which state it's currently in.
        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text != "Following":
            followButton.click()
            time.sleep(2)
        else:
            print("Already following this account")

    def unFollowUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text == "Following":
            followButton.click()
            time.sleep(2)
            # Clicking "Following" opens a confirmation popup with an
            # "Unfollow" button; this XPath finds a <button> whose visible
            # text is exactly "Unfollow" (text()="..." checks a tag's text
            # content directly inside the XPath expression) and clicks it.
            self.browser.find_element_by_xpath('//button[text()="Unfollow"]').click()
        else:
            print("Not following this account anyway.")


instgrm = Instagram(username, password)
instgrm.signIn()
instgrm.getFollowers(50)
# instgrm.followUser('example_user')
# instgrm.unFollowUser('example_user')

# usernames = ["example_user",""]

# for user in usernames:
#     instgrm.followUser(user)
#     time.sleep(3)
