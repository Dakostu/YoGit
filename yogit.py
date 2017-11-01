# Yo Git! 
# 2017 Daniel Kostuj
# GPL V2 License
# This script will open a random URL of a GitHub repository that has been recently modified.

import webbrowser 
import random
import urllib
import re
from six.moves.urllib.request import urlopen
from datetime import date, timedelta

# Get today timestamp for advanced search
today = date.today()
yesterday= date.today() - timedelta(1)
todayDay = today.strftime("%d")
todayMonth = today.strftime("%m")
todayYear = today.strftime("%Y")
yesterdayDay = yesterday.strftime("%d")
yesterdayMonth = yesterday.strftime("%m")
yesterdayYear = yesterday.strftime("%Y")
gitHubURL = "https://github.com"
urlList = []
# RegEx blacklist 
blacklist = "(?!assets|articles|site|images|open_graph|features|business|_private|docs|blog|about|integrations|modules|pricing|feature|browser|search|trending|topics|unicode|devops|icons|pulls|issues|marketplace|explore|organizations|site|security|github-external|new|contact|[\w\-\_\.]*github)"
# regular expression for "/user-name/name-of-repository"
regEx = "/+" + blacklist + "[[\w\-\_\.]+/[\w\-\_\.]*]*"

# skim through first three search result pages
# and filter out repository URL into a list
for i in range(1,4):
    # URL for advanced search:
    # p=i: open page number i
    # q=created: created on a certain day
    # s=updated: sort by most recent update
    searchUrl = gitHubURL + "/search?p=" + str(i) + "&q=created%3A" + todayYear + "-" + todayMonth + "-" + todayDay + "&q=created%3A" + yesterdayYear + "-" + yesterdayMonth + "-" + yesterdayDay + "&s=updated&type=Repositories"
    
    try:
        fileDesc = urlopen(searchUrl)
    except urllib.error.HTTPError as e:
        print ("HTTP Error: " + str(e.code))
        raise SystemExit
    except urllib.error.URLError as e:
        print ("Error while accessing Github pages:")
        print (str(e.reason))
        print ("Please check your connection status.")
        raise SystemExit
    
    pagesStringified = fileDesc.read().decode()
    urlList += re.findall(regEx,pagesStringified)
    
if len(urlList) == 0:
           print ("No Repositories found.")
           raise SystemExit
    
# get random element from list and open in browser
random.seed()
randomRepoLink = urlList.pop(random.randrange(len(urlList)))
webbrowser.open(gitHubURL + randomRepoLink, new=2, autoraise=True)



