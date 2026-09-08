# themoviedb.org => movie and TV show database
# Use the API that themoviedb provides in your own application.
# Search by keyword
# List of most popular movies
# List of movies currently in theaters

# This script wraps a couple of TheMovieDB (TMDb) API endpoints in a class,
# the same pattern used in github.py: build the request URL, call
# requests.get(), and parse the JSON response with .json().
import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        # TMDb requires an API key on every request to identify the calling
        # application. You must sign up for a free TMDb account and replace
        # this placeholder with your own key for these calls to work.
        self.api_key = "<your_api_key>"

    def getPopulars(self):
        # Query string parameters after the "?" configure the request:
        #   api_key  -> your TMDb API key (authentication)
        #   language -> which language to return titles/text in
        #   page     -> which page of results to fetch (TMDb paginates results)
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self, keyword):
        # The "query" parameter carries the search keyword the user typed.
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movieApi = theMovieDb()

while True:
    choice = input("1-Popular Movies\n2-Search Movies\n3-Exit\nChoice: ")

    if choice == "3":
        break
    else:
        if choice == "1":
            movies = movieApi.getPopulars()
            # TMDb wraps the actual list of movies inside a "results" key
            # of the parsed JSON dict, alongside pagination info like
            # "page" and "total_results" (not used here).
            for movie in movies['results']:
                print(movie['title'])

        if choice == "2":
            keyword = input('keyword: ')
            movies = movieApi.getSearchResults(keyword)
            # Note: the /search/keyword endpoint's results represent
            # matching KEYWORD tags (each with a 'name'), not movies with a
            # 'title' - the code below reads 'name', matching that shape.
            for movie in movies['results']:
                print(movie['name'])
