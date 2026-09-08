# First time parsing HTML with BeautifulSoup instead of regex - much less painful.
#
# BeautifulSoup is a library that turns a blob of HTML text into a tree of
# Python objects you can navigate and search - similar to how a web browser
# turns HTML into a DOM. Trying to pull data out of HTML with regular
# expressions gets painful fast (HTML nesting, attributes in any order,
# self-closing tags, ...), so BeautifulSoup is the standard tool for this.
html_doc = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>My First Web Page</title>
</head>
<body>

    <h1 id="header">
        Python Course
    </h1>

    <div class="grup1">
        <h2>
            Programming
        </h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>
            Modules
        </h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>

    <!-- fred.jpg is just a placeholder cartoon image for the img tag exercise -->
    <img src="fred.jpg" alt="">

    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>
"""


from bs4 import BeautifulSoup

# BeautifulSoup(markup, parser_name) parses the given HTML string and returns
# a "soup" object representing the whole document as a navigable tree.
# "html.parser" is Python's built-in HTML parser (no extra install needed);
# other options like "lxml" or "html5lib" exist too, but need to be
# installed separately and are only faster/more lenient, not required here.
soup = BeautifulSoup(html_doc, 'html.parser')

# .prettify() returns the document as a nicely indented string - handy for
# checking that the HTML was parsed the way you expect.
result = soup.prettify()

# Accessing a tag name as an attribute (soup.title, soup.head, soup.body,
# soup.h1, soup.h2, soup.div, ...) is BeautifulSoup's shortcut for "find the
# FIRST tag with this name anywhere in the document". It's short to write,
# but only ever gives you the first match, never a list.
result = soup.title
result = soup.head
result = soup.body

# Every tag object has a couple of useful properties:
#   .name   -> the tag's name as a string, e.g. "title"
#   .string -> the text directly inside the tag (only works cleanly when the
#              tag contains just one piece of text and no nested tags)
result = soup.title.name
result = soup.title.string

result = soup.h1
result = soup.h2
result = soup.h2.name
result = soup.h2.string
result = soup.h1.string

# .find_all(tag_name) searches the WHOLE document and returns a list of
# every matching tag (as opposed to soup.h2, which only returns the first
# one). There are three <h2> tags in the document above ("Programming",
# "Modules", "Django"), so this returns a list of all three, and indexing
# into that list with [0] / [1] picks out a specific one.
result = soup.find_all('h2')
result = soup.find_all('h2')[0]
result = soup.find_all('h2')[1]

# soup.div is shorthand for "the first <div> in the document" (the one with
# class="grup1"). find_all('div')[1] instead explicitly grabs the SECOND
# <div> in document order (class="grup2"), and then .ul.find_all('li') dives
# into that div's <ul> child and pulls out all of its <li> items - showing
# that you can chain lookups to walk down the tree step by step.
result = soup.div
result = soup.find_all('div')[1]
result = soup.find_all('div')[1].ul.find_all('li')

# .findChildren() returns every descendant tag nested inside soup.div (its
# <h2> and its <ul> with all of its <li> items), not just its direct children.
result = soup.div.findChildren()

# BeautifulSoup also lets you move sideways/around the tree relative to a
# tag you already have, instead of always searching from the top:
#   .findNextSibling()     -> the next tag at the same nesting level
#   .findPreviousSibling() -> the previous tag at the same nesting level
# Starting from the first <div> (class="grup1"), findNextSibling() moves to
# the second <div> (class="grup2"), findNextSibling() again moves to the
# third <div> (class="grup3"), and then findPreviousSibling() steps back one,
# landing us back on the second <div> (class="grup2").
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()

# find_all('a') collects every <a> (anchor/link) tag in the document - here,
# the three "Elsie" links - into a list.
result = soup.find_all('a')

# Each tag behaves a bit like a dictionary for its HTML attributes: .get('href')
# reads the value of the href="..." attribute (returns None if the tag
# doesn't have that attribute). This loop prints each link's URL:
# http://example1.com/elsie, http://example2.com/elsie, http://example3.com/elsie
for link in result:
    print(link.get('href'))
