#Gautam Mehta
#Aiden Sun
#Chris Gentibano
import json
import sqlite3

# Allowed a one day extension on this lab

def countryMatch(d):
    first_letter = input('First letter of country name: ')

    
    while first_letter.upper() not in d:
        first_letter = input('First letter of country name: ')    
        
    countryList= d.get(first_letter.upper())
    countryList = ["{}: {}".format(i,country) for i, country in enumerate(list(countryList),1)]        
    print ("Countries:")
    for i in countryList:
        print(i)
    return countryList

def validateNum(num, countryList):
    newlist = [i[0] for i in countryList]
    while num not in newlist:
        print ("Invalid input chosen from the country list. Please try again")
        num = str(input("Type in a new number: "))
    return num

def getAth(num,countryList, cur):
    onlyCtry = [i[3:] for i in countryList]
    for i in countryList:
        if num == i[0]:
            country= onlyCtry[int(num)-1]
    cur.execute("SELECT TotAthletes FROM Countries WHERE country = ?", (country,))
    ath= str(cur.fetchone())
    print(ath[1:-2], "athletes for", country)   
    

def displaySport(cur):
    print("Sports:")
    sportsList=[]
    for sport in cur.execute("SELECT * FROM Sports"):
        sportsList.append(sport[1])
    print(', '.join(sportsList))
    return sportsList

def countryParticipate(sportsList, cur):
    sportName = input("Enter sport name: ").title()
    
    while sportName not in sportsList:
        sportName = input('Invalid entry. Re-enter the sport name: ').title()
    cur.execute('''SELECT Countries.country 
                   FROM Countries JOIN Sports
                   ON Countries.S1 = Sports.sid AND Sports.sports= ? OR Countries.S2 = Sports.sid AND Sports.sports= ?
                   OR Countries.S3 = Sports.sid AND Sports.sports= ? OR Countries.S4 = Sports.sid AND Sports.sports= ?
                   OR Countries.S5 = Sports.sid AND Sports.sports= ? OR Countries.S6 = Sports.sid AND Sports.sports= ?
                   OR Countries.S7 = Sports.sid AND Sports.sports= ? OR Countries.S8 = Sports.sid AND Sports.sports= ?
                   OR Countries.S9 = Sports.sid AND Sports.sports= ? OR Countries.S10 = Sports.sid AND Sports.sports= ?
                   OR Countries.S11 = Sports.sid AND Sports.sports= ? OR Countries.S12 = Sports.sid AND Sports.sports= ?
                   OR Countries.S13 = Sports.sid AND Sports.sports= ? OR Countries.S14 = Sports.sid AND Sports.sports= ?
                   OR Countries.S15 = Sports.sid AND Sports.sports= ? ORDER by country''', (sportName,sportName,sportName,sportName,
                                                                           sportName,sportName,sportName,sportName,
                                                                           sportName,sportName,sportName,sportName,
                                                                           sportName,sportName,sportName,))
    for record in cur.fetchall() :
        print(record[0])

def displayMax(min1, max1, cur):
    print("Countries with", min1, "to", max1, "athletes")
    cur.execute("SELECT Countries.country FROM Countries WHERE TotAthletes BETWEEN ? AND ? ORDER by country", (min1,max1))
    for record in cur.fetchall() :
        print(record[0])     
# I am not using the numeric compare here with WHERE clause and I still yield same result but with Australia
# I understand that this is acceptable after looking at discussion 

def main():
    with open('olympics.json', 'r') as fh:
        d = json.load(fh)
        
    conn = sqlite3.connect('olympics.db')
    cur = conn.cursor()
    
    cL = countryMatch(d)
    number = str(input("Enter in a number: "))
    validNum = validateNum(number, cL)
    getAth(validNum,cL, cur)
    
    print()
    
    sL = displaySport(cur)
    countryParticipate(sL,cur)
    
    print()
    min1, max1 = input("Enter min, max number of athletes: ").split(', ')
    displayMax(min1,max1, cur)
    conn.close()
    
main()    
