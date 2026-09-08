# Small scraper that logs into GitHub and collects a user's follower list.
# First time I used Selenium to drive a real login form instead of just reading a page.
#
# Selenium is different from requests+BeautifulSoup: instead of just
# downloading a page's raw HTML, it drives an ACTUAL browser (here, Chrome)
# - typing into fields, clicking buttons, waiting for JavaScript to run -
# exactly like a human user would. That's necessary for pages that require
# login, or that build their content dynamically with JavaScript after the
# initial page load.
#
# NOTE: this script automates GitHub's real login page and follower list by
# clicking through elements picked out with hardcoded XPath expressions.
# Any redesign of github.com's page structure (which happens over time) can
# break these selectors - this is not guaranteed to still work as-is.
from githubUserInfo import username, password
from selenium import webdriver
import time

class Github:
    def __init__(self, username, password):
        # webdriver.Chrome() launches a real, visible Chrome browser window
        # that Selenium will control programmatically. It requires a
        # matching "chromedriver" executable to be available (installed or
        # on PATH) - chromedriver is the bridge program Selenium talks to in
        # order to control Chrome.
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        # .get(url) navigates the browser to the given address, just like
        # typing it into the address bar and pressing Enter.
        self.browser.get("https://github.com/login")
        # time.sleep(seconds) pauses the script (not the browser) for a
        # fixed amount of time. It's a simple - if slightly crude - way to
        # give the page time to finish loading before we try to interact
        # with it; Selenium also offers smarter "explicit waits" that wait
        # only until a specific element appears, but this script always
        # uses the simpler fixed-delay approach.
        time.sleep(2)

        # find_element_by_xpath(expr) locates a single element in the page
        # using an XPath expression - a path-like syntax for navigating an
        # HTML/XML document. "//*[@id='login_field']" means "anywhere in the
        # document (//), any tag (*), whose id attribute equals 'login_field'".
        # .send_keys(text) then types that text into the located element,
        # exactly as if a user had typed it on the keyboard.
        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        # This XPath is far more specific/brittle: it walks down an exact
        # chain of parent-child elements ("//*[@id='login']/form/div[3]/input[8]")
        # to reach the sign-in button. Long, position-based XPaths like this
        # are especially likely to break if GitHub reorders the form's markup.
        self.browser.find_element_by_xpath("//*[@id='login']/form/div[3]/input[8]").click()

    def loadFollowers(self):
        # find_elements_by_css_selector (plural "elements") returns a LIST
        # of every element matching a CSS selector, as opposed to
        # find_element_by_... (singular), which returns just the first
        # match. ".d-table.table-fixed" selects elements that have BOTH the
        # "d-table" AND "table-fixed" CSS classes at once (a dot before a
        # name matches a class; two dotted names back-to-back means "has
        # both classes").
        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")

        for i in items:
            # Inside each follower "row" element, find the one small link
            # holding the username text, and collect its visible text
            # (.text) into our running list of followers.
            self.followers.append(i.find_element_by_css_selector(".link-gray.pl-1").text)


    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)

        # pagination: GitHub splits followers across pages, so we keep clicking "Next"
        self.loadFollowers()

        while True:
            # find_element_by_class_name looks up an element by exactly one
            # CSS class name (no dot needed, unlike a CSS selector).
            # .find_elements_by_tag_name("a") then collects every <a> (link)
            # element inside that button group - GitHub's pagination
            # controls are rendered as one or more link/button elements
            # inside a "BtnGroup" container.
            links = self.browser.find_element_by_class_name("BtnGroup").find_elements_by_tag_name("a")

            if len(links) == 1:
                # Only one pagination link present - it's either "Next" (if
                # we're not on the last page yet) or something else (in
                # which case we've reached the end and stop).
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadFollowers()

                else:
                    break
            else:
                # Multiple pagination links (e.g. both "Previous" and
                # "Next") - search through them for the one labeled "Next"
                # specifically, ignoring the others.
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)
                        self.loadFollowers()
                    else:
                        continue


github = Github(username, password)
github.signIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)


