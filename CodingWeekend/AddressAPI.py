import urllib, os
import flask
import urllib.request
import sqlite3
import requests
import sys



myloc = r"/Users/gautammehta/Desktop/CodingWeekend/" #replace with your own location
key = "&key=" + "" 

def databaseExtraction():
    conn = sqlite3.connect('Monuments.db')
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor() # used to issue sql commands
    addresses=[]
    for record in cur.execute("SELECT address FROM Monument") : # * means every single query in the database
        addresses.append(record)
    return addresses
def GetStreet(Add,SaveLoc):
    base = "https://maps.googleapis.com/maps/api/streetview?size=1200x800&location="
    MyUrl = base + urllib.parse.quote_plus(Add) + key #added url encoding
    fi = Add + ".gif"
    urllib.request.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))

Tests = databaseExtraction()

for i in Tests:
    GetStreet(Add=i,SaveLoc=myloc)
