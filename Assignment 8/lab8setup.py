#Gautam Mehta
#Aiden Sun
#Chris Gentibano 
from bs4 import BeautifulSoup
import requests
import re
import sys
import json
import sqlite3

LINK = 'https://www.olympic.org/pyeongchang-2018/results/en/general/nocs-list.htm'

def getCountries(LINK):
    try:
        page = requests.get(LINK)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, 'lxml')
        countryList = [text.get_text() for text in soup.select("div.CountriesListItem a.center-block strong")]
        linkList= ["https://www.olympic.org/pyeongchang-2018/results"+ str(link.get('href'))[5:] for link in soup.select("div.CountriesListItem a.center-block")]
        masterList= list(zip(countryList,linkList))
        sportsPage = requests.get(linkList[91])
        soup2 = BeautifulSoup(sportsPage.content, 'lxml')
        sportsList = [sports.get_text() for sports in soup2.select('table.ResTableFull td strong')]  
        sportsList= sportsList[:15]
        sorted(masterList)
        
        totalAthl = []
        ctrySports = []
        
        for x in linkList:
            page = requests.get(x)
            soup = BeautifulSoup(page.content, "lxml")
            
            # grabs the total athletes
            for data in soup.select('tr.MedalStd1 td'): 
                totalNum = data.get_text().strip()
            totalAthl.append(totalNum) #this is the list of total athletes per country
            
            # grabs sports attended
            for data in soup.select('table.ResTableFull strong'):
                ctrySports.append(data.get_text().strip())
            ctrySports.append("") # if data is done for one country, appends blank space.
            
    except requests.exceptions.HTTPError as error:
        print (error)
        sys.exit()
    except requests.exceptions.RequestException as e:
        print (e)
        sys.exit("Unable to access requested URL")
    except requests.exceptions.Timeout:
        sys.exit("Unable to access requested URL")
    except requests.exceptions.TooManyRedirects:
        sys.exit("Unable to access requested URL")

    return masterList, sportsList, totalAthl, ctrySports, countryList

def createJSON(countryList):
    countryList = "','".join(map(str,countryList))
    d={}
    for word in countryList.split("','"):
        if(word[0] not in d.keys()):
            d[word[0]]=[]
            d[word[0]].append(word)
        else:
            if(word not in d[word[0]]):
                d[word[0]].append(word)
                
    with open('olympics.json', 'w') as fh:
        json.dump(d, fh, indent=3)  
     
def createDB(countries,sportsList,athletes,ctrySports):
    conn = sqlite3.connect('olympics.db')
    cur = conn.cursor() # used to issue sql commands
    
    cur.execute("DROP TABLE IF EXISTS Countries")   
    cur.execute('''CREATE TABLE Countries(
                       cid INTEGER NOT NULL PRIMARY KEY,
                       country TEXT,
                       TotAthletes INT,
                       S1 INT,
                       S2 INT,
                       S3 INT,
                       S4 INT,
                       S5 INT,
                       S6 INT,
                       S7 INT,
                       S8 INT,
                       S9 INT,
                       S10 INT,
                       S11 INT,
                       S12 INT,
                       S13 INT,
                       S14 INT,
                       S15 INT)''')

    cur.execute("DROP TABLE IF EXISTS Sports")  
    cur.execute('''CREATE TABLE Sports(
                       sid INTEGER NOT NULL PRIMARY KEY,
                       sports TEXT)''')
    
    for x in countries:
        cur.execute("INSERT INTO Countries (country) VALUES (?)", (x[0:1])) 
        
    for y in sportsList:
        cur.execute("INSERT INTO Sports (sports) VALUES (?)", (y,))
    
    i = 1
    for y in athletes:
        cur.execute("UPDATE Countries SET TotAthletes = ? WHERE cid = ?", (y,i)) 
        i += 1
    
    ctr = 0
    foundList = []
    
    i = 1
    for x in ctrySports: 
        if x == '':
            for x in range(ctr): #amount of times found, will iterate through
                if (x == 0):
                    cur.execute("UPDATE Countries SET S1 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 1):
                    cur.execute("UPDATE Countries SET S2 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 2):
                    cur.execute("UPDATE Countries SET S3 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 3):
                    cur.execute("UPDATE Countries SET S4 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 4):
                    cur.execute("UPDATE Countries SET S5 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 5):
                    cur.execute("UPDATE Countries SET S6 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 6):
                    cur.execute("UPDATE Countries SET S7 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 7):
                    cur.execute("UPDATE Countries SET S8 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 8):
                    cur.execute("UPDATE Countries SET S9 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 9):
                    cur.execute("UPDATE Countries SET S10 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 10):
                    cur.execute("UPDATE Countries SET S11 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 11):
                    cur.execute("UPDATE Countries SET S12 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 12):
                    cur.execute("UPDATE Countries SET S13 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 13):
                    cur.execute("UPDATE Countries SET S14 = ? WHERE cid = ?", (foundList[x],i))
                elif (x == 14):
                    cur.execute("UPDATE Countries SET S15 = ? WHERE cid = ?", (foundList[x],i))                
                else:
                    break
            ctr = 0
            i += 1
            foundList = []
        else:
            if x in sportsList:
                ctr += 1
                foundList.append(sportsList.index(x) + 1)
    conn.commit()
    conn.close()

def main():
    countries, sportsList, totalAthl, ctrySports, cL = getCountries(LINK)
    createDB(countries,sportsList, totalAthl, ctrySports)
    createJSON(cL)
             
main()