# Yo Git! 
# 2017 Daniel Kostuj
# GPL V2 License
# This script will open a random URL of a GitHub repository that has been recently modified.

import requests
import random
import webbrowser 
from datetime import date, timedelta

# put a date into an ISO date string
def putInISO(aDate):
    return aDate.strftime("%Y") + "-" + aDate.strftime("%m") + "-" + aDate.strftime("%d")
    
# This is where the magic happens
def main():    
    gitHubURL = "https://github.com/"
    # Get today's and yesteday's timestamp for advanced search
    today = date.today()
    todayISO = putInISO(today)
    yesterday = today - timedelta(days = 1)
    yesterdayISO = putInISO(yesterday)

    # open list of 100 most recent repositories on GitHub API
    urlList = requests.get('https://api.github.com/search/repositories', params = {"sort": "updated", "order" : "desc", "q" : "created:>" + todayISO, "q" : "created:>" + yesterdayISO, "per_page" : "100"})
    
    # get random element from list and open in browser    
    random.seed()
    randomRepoLink = urlList.json()["items"][random.randrange(100)]["full_name"]
    webbrowser.open(gitHubURL + randomRepoLink, new=2, autoraise=True)


main()
