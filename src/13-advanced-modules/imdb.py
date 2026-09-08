# Scraping the IMDb top 250 chart - my first real-world (not toy) BeautifulSoup exercise.
#
# "Web scraping" means downloading a real webpage's HTML and extracting data
# out of it programmatically, as opposed to using an official API. It's more
# fragile than an API because the result depends entirely on the page's
# current HTML structure - if IMDb changes their page layout or class names,
# this script would need updating (or may already need updating by the time
# you read this, since websites change their markup over time and IMDb's
# real chart page structure has evolved past what's assumed here).
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

# requests.get(url).content downloads the raw page and gives us the response
# body as raw bytes (.content) rather than as a decoded string (.text) -
# BeautifulSoup can parse either, but bytes let it auto-detect the page's
# character encoding itself.
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

# find(tag, attrs) returns the FIRST matching tag - here, the <tbody> whose
# class attribute contains "lister-list" (the table body holding the movie
# rows). {"class": "lister-list"} is how you filter find()/find_all() by an
# HTML attribute instead of just by tag name.
# .find_all("tr", limit=50) then collects up to 50 <tr> (table row) tags
# inside that tbody - the "limit" argument caps how many matches are
# returned, so we only get the first 50 rows even if there are more.
rows = soup.find("tbody", {"class":"lister-list"}).find_all("tr",limit=50)
count = 1

for tr in rows:
    # Within each row, drill into the cell holding the title (<td
    # class="titleColumn">) and pull out the text of its <a> (link) tag -
    # that's the movie's title.
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    # The same titleColumn cell also contains a <span> with the release
    # year in parentheses, e.g. "(1994)". .strip("()") removes leading and
    # trailing parenthesis characters from the text, leaving just "1994".
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    # The rating lives in a separate cell whose class is the two words
    # "ratingColumn imdbRating" - BeautifulSoup matches on the full class
    # attribute string. Inside it, the numeric rating is wrapped in a
    # <strong> tag.
    rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text

    # .ljust(50) pads the title with spaces on the right until it's 50
    # characters wide, so the year/rating columns line up neatly when
    # printed, regardless of how long each movie's title is.
    print(f"{count}- movie: {title.ljust(50)} year: {year} rating: {rating}")
    count+=1
