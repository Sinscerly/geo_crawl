import requests
import string
import re
from datetime import *
from bs4 import BeautifulSoup as soup

#geocacheCode = "GC868JC"

class cacheInfo(object):
    def __init__(self, geoCode):
        self.geoCode = geoCode
        url = requests.get('https://www.geocaching.com/geocache/' + self.geoCode)
        self.source = soup(url.text, 'html.parser')
        #owner, date
        self.minorCacheDetails = self.source.find("div", {"class": "minorCacheDetails Clear"})
        #founds, not founds, write note, publisher notes
        self.logTotals = re.sub(r'\<.*?\>|\s{2,}', "", str(self.source.find("p", {"class": "LogTotals"}))).lstrip().split(" ")
    def get_owner(self):
        owner = self.minorCacheDetails.find("div", {"id": "ctl00_ContentBody_mcd1"})
        owner = re.sub(r'\<.*?\>', "", str(owner)).lstrip().replace("\n\n", "").split("\n")
        self.owner = owner[0].replace("A cache by ", "")
        return self.owner
    def get_name(self):
        name = self.source.find("span", {"id": "ctl00_ContentBody_CacheName"})
        self.name = re.sub(r'\<.*?\>', "", str(name))
        return self.name
    def get_datePlaced(self):
        date = self.minorCacheDetails.find("div", {"id": "ctl00_ContentBody_mcd2"})
        date = date.get_text().replace(" ", "").replace("\n", "").split(":")[1]
        return date_rewrite(date)
    def get_daysOld(self):
        x = self.get_datePlaced()
        return time_from(x)
    def get_lastFind(self):
        scrap = self.source.findAll("small")
        bottem = re.sub(r'\<br/\>', "\n", str(scrap[3]))
        bottem = re.sub(r'\<.*?\>', "", str(bottem))
        return date_rewrite(bottem.split("\n")[2].split(" ")[2])
    def get_dayslastFind(self):
        x = self.get_lastFind()
        return time_from(x)
    def get_finds(self):
        return int(self.logTotals[0])
    def get_doNotFinds(self):
        if ("Didn't find it" in str(self.source.find("p", {"class": "LogTotals"}))):
            return int(self.logTotals[1])
        else:
            return 0
    def get_writeNotes(self):
        return int(self.logTotals[2])
    def get_favo(self):
        #works only if you're logged in...
        scrap = self.source.find("div", {"class": "span-17"})
        print(scrap)
        favo = re.sub(r'\<.*?\>', "", str(scrap))
        return favo

def date_rewrite(x):
    date = x.split("/")
    return (date[1] + "/" + date[0] + "/" + date[2])	
def time_from(x):
    x = x.split("/")
    return (date.today() - date(int(x[2]),int(x[1]),int(x[0]))).days 

#c = cacheInfo("gc8aj4t")
#print(c.get_name() + ", a cache from: " + c.get_owner())
#print(c.get_datePlaced())
#print(c.get_daysOld())
#print(c.get_finds())
#print(time_from(c.get_lastFind()))
#print(c.get_favo())


