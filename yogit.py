# Yo Git! 
# 2017 Daniel Kostuj
# GPL V2 License
# This script will open a random URL of a GitHub repository that has been recently modified.

import webbrowser 
import random
import time
import urllib
import re
from six.moves.urllib.request import urlopen

# Get current timestamp for advanced search
currentDay = time.strftime("%d")
currentMonth = time.strftime("%m")
currentYear = time.strftime("%Y")
gitHubURL = "https://github.com"
urlLists = []
# RegEx blacklist 
blacklist = "(?!assets|articles|site|images|open_graph|features|business|_private|docs|integrations|modules|pricing|feature|browser|search|trending|topics)"
# regular expression for "/username/name-of-repository"
regEx = "/+" + blacklist + "[[\w]+/[\w\-\_\.]*]*"


# skim through first three search result pages
# and filter out repository URL into a list
for i in range(1,4):
    # URL for advanced search:
    # p=i: open page number i
    # q=created: created on current day
    # s=updated: sort by most recent update
    searchUrl = gitHubURL + "/search?p=" + str(i) + "&q=created%3A" + currentYear + "-" + currentMonth + "-" + currentDay + "&s=updated&type=Repositories"
    fileDesc = urlopen(searchUrl)
    pagesStringified = fileDesc.read().decode()
    urlLists += re.findall(regEx,pagesStringified)
    
# get random element from list and open in browser
randomRepoLink = urlLists.pop(random.randrange(len(urlLists)))
webbrowser.open(gitHubURL + randomRepoLink, new=2, autoraise=True)



