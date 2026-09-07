# themoviedb.org => movie and TV show database
# Use the API that themoviedb provides in your own application.
# Search by keyword
# List of most popular movies
# List of movies currently in theaters

import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "<your_api_key>"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self, keyword):
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
            for movie in movies['results']:
                print(movie['title'])

        if choice == "2":
            keyword = input('keyword: ')
            movies = movieApi.getSearchResults(keyword)
            for movie in movies['results']:
                print(movie['name'])