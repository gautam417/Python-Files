#Gautam Mehta
#Aiden Sun

'''
At the beginning of the program, one request is made to the main website and all the countries' data is stored in a list
of tuples (country name, link). Then the program asks the user to select the country.
Then the program makes one specific request to get the user's country's page and those data is stored in a string.
Finally, the program does the formatting and prints desired data. Note that this, program only makes two requests to server. 

This is better than sending one request to the main page to collect country data, then sending a request for each country's page
to collect all the data, and finally asks the user to pick which data to display. Note that each request takes time, and data that is not picked
by the user will be using unncessary memory. 
'''

from bs4 import BeautifulSoup
import requests
import re
import sys

LINK = 'https://www.olympic.org/pyeongchang-2018/results/en/general/nocs-list.htm'

def getCountries(LINK):
    try:
        page = requests.get(LINK)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, 'lxml')
        countryList = [text.get_text() for text in soup.select("div.CountriesListItem a.center-block strong")]
        linkList= ["https://www.olympic.org/pyeongchang-2018/results"+ str(link.get('href'))[5:] for link in soup.select("div.CountriesListItem a.center-block")]
        masterList= list(zip(countryList,linkList))
        sorted(masterList)
        
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
        
    return masterList

def getScores(userList, masterList):
    num = str(input("Type in a number: "))
    num = validateNum(num, userList)
    for i in userList:
        if num == i[0]:
            countryName = i[3:]
            print('Data for', countryName)
            for i in masterList:
                if i[0] == countryName:
                    dataPage = requests.get(i[1])
                    soup = BeautifulSoup(dataPage.content, "lxml") 
                    header = soup.find('table', class_='ResTableFull')
                    text = header.get_text()                     
    
    return text

def printTabular(text):
    myText = [line.strip() for line in text.splitlines() if line.strip()]
    row_format = '{:>30} {:>6} {:>6} {:>10} \n' * (len(myText)//4)
    print(row_format.format(*myText))    

def matchCountries(char, countries):
    regex= re.compile(char, re.I)
    countryList = [i[0] for i in countries] #update country list to be sorted with just the country list (no link)
    userList = filter(regex.match, countryList)
    userList = ["{}: {}".format(i,country) for i, country in enumerate(list(userList),1)]        
    
    print ("Countries participating in the Winter Olympics:")
    for i in userList:
        print(i)    

    return userList

def validateNum(num, userList):
    newlist = [i[0] for i in userList]
    while num not in newlist:
        print ("Invalid input chosen from the country list. Please try again")
        num = str(input("Type in a new number: "))
        
    return num

def validateChar(char, countryList):
    while not char.isalpha():
        print('Please try entering in a valid country name again')
        char = input('First letter of country name: ')
        if char == '0':
            sys.exit('Program is ending, goodbye!')     
        
    newList = [i[0] for i in countryList]
    first_letters = [i[0] for i in newList]
    while char.upper() not in first_letters:
        print("No match found in the list of countries partcipating in Olympics. Please try another first letter")
        char = input('First letter of country name: ')
        if char == '0':
            sys.exit('Program is ending, goodbye!')         
    return char

def main():
    countries = getCountries(LINK)
    while True:
        first_letter = input('First letter of country name: ')
        
        if first_letter == '0':
            print('Program is ending, goodbye!')
            break       
        
        char = validateChar(first_letter, countries)
        userList = matchCountries(char, countries)
        data = getScores(userList, countries)
        printTabular(data)
             
main()