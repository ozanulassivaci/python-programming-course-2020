# Scraping a laptop listing page - practicing pulling out price/name/link from repeated cards.
#
# n11.com is a Turkish e-commerce site; this script scrapes its laptop
# category page. Like the IMDb example, this depends entirely on n11's
# current HTML structure - e-commerce sites redesign their listing pages
# fairly often, so the class names used below ("column", "proDetail") may
# no longer match the live site by the time this is run.
import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

# Each product on the page is rendered as its own <li class="column"> -
# find_all collects every one of these "product card" list items into a list.
items = soup.find_all("li",{"class":"column"})

for li in items:
    # Chaining tag names directly (li.div.a.h3) walks straight down the tree:
    # the <li>'s first <div>, that div's first <a>, that a's first <h3> -
    # equivalent to, but shorter than, calling .find() three times in a row.
    # .strip() removes leading/trailing whitespace/newlines that HTML
    # indentation often leaves around text.
    name = li.div.a.h3.text.strip()
    # .get("href") reads the link's URL from its href="..." attribute.
    link = li.div.a.get("href")
    # Inside the "proDetail" div there are (at least) two <a> tags: the
    # first holds the old/original price, the second the discounted price.
    # .strip('TL') removes the currency suffix "TL" (Turkish Lira) from the
    # text (as well as any leading/trailing characters that happen to be
    # 'T' or 'L', since strip() removes any of the given characters, not
    # the exact substring "TL" as a whole).
    oldprice = li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip('TL')
    newprice = li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip('TL')

    print(f"name: {name} link: {link} old price: {oldprice} new price: {newprice}")
