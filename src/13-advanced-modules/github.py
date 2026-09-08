# Wrapping the GitHub REST API in a small class instead of calling requests directly everywhere.
#
# GitHub exposes a public REST API (https://api.github.com) that returns
# JSON data about users, repositories, etc, and also lets you create
# resources (like a new repository) by sending data TO it, not just reading
# data FROM it. This script wraps a few of those endpoints in a class so the
# rest of the code can call friendly method names instead of repeating full
# URLs everywhere.
import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        # A "personal access token" is how you prove your identity to the
        # GitHub API for actions that require being logged in (like creating
        # a repository). Never commit a real token to source control - this
        # placeholder must be replaced with your own token to actually run
        # createRepository().
        self.token = '<your_access_token>'

    def getUser(self, username):
        # GET /users/{username} is a public, read-only endpoint - no token
        # needed just to look up basic profile info about a user.
        response = requests.get(self.api_url+'/users/'+ username)
        # .json() is a shortcut on the Response object that does the same
        # thing as json.loads(response.text): parses the JSON response body
        # into a native Python dict/list in one step.
        return response.json()

    def getRepositories(self,username):
        # GET /users/{username}/repos returns a JSON array (a Python list,
        # once parsed) of that user's public repositories.
        response = requests.get(self.api_url+'/users/'+ username+'/repos')
        return response.json()

    def createRepository(self, name):
        # requests.post(url, json={...}) sends an HTTP POST request - the
        # kind used to CREATE something on the server - with the given
        # dictionary automatically encoded as a JSON request body. This is
        # the write counterpart to requests.get(), and it's why it needs the
        # access token appended to the URL: creating a repo requires being
        # authenticated as a specific GitHub account.
        response = requests.post(self.api_url+'/user/repos?access_token='+ self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://example.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()

github = Github()

while True:
    choice = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nChoice: ')

    if choice == '4':
        break
    else:
        if choice == '1':
            username= input('username: ')
            result = github.getUser(username)
            # Reading specific fields back out of the JSON dict GitHub returned.
            print(f"name: {result['name']} public repos: {result['public_repos']}  follower : {result['followers']}")
        elif choice == '2':
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif choice == '3':
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print('invalid choice')
