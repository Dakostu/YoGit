# Yo Git! 
# 2017 Daniel Kostuj
# GPL V2 License
# This script will open a random URL of a GitHub repository that has been recently modified.

import requests
import random
import webbrowser 
from datetime import date, timedelta

# function: transform date into ISO date string format
def putInISO(aDate):
    return aDate.strftime("%Y") + "-" + aDate.strftime("%m") + "-" + aDate.strftime("%d")
    
# This is where the magic happens
def main():    
    # Get timestamp of the day before yesterday as a buffer for API request
    pufferDay = date.today() - timedelta(days = 2)
    pufferDayISO = putInISO(pufferDay)

    # open list of 100 most recent repositories on GitHub API
    try:
        urlList = requests.get('https://api.github.com/search/repositories', params = {"sort": "updated", "order" : "desc", "q" : "created:>" + pufferDayISO, "per_page" : "100"})
    except requests.exceptions.RequestException as e:
        print ("GitHub API could not be accessed at this time:")
        print (e)
        raise SystemExit
    
    # get random element from list and open in browser    
    random.seed()
    randomRepoLink = urlList.json()["items"][random.randrange(100)]["html_url"]
    webbrowser.open(randomRepoLink, new=2, autoraise=True)



if __name__ == "__main__":
    main()
