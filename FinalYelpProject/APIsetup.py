#Gautam Mehta, Chris Gentibano, Aiden Sun
from __future__ import print_function
import json
import sqlite3
import requests
import sys
import urllib
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode
from operator import itemgetter

API_KEY= "YOUR API KEY HERE"
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'


def request(host, path, api_key, url_params= {'term': "Fast Food", 'limit': 50,'latitude':37.319540,
                                              'longitude':-122.045055, 'radius': 8046}):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """    
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))
    response = requests.request('GET', url, headers=headers, params=url_params)
    jDict= response.json()
    businesses = jDict.get('businesses')
    print()

    if not businesses:
        print('No businesses found.')
        return    
    print(u'{0} businesses found'.format(len(businesses)))    
    with open('bussinesses.json', 'w') as fh:
        json.dump(jDict, fh, indent=5)         

    name = (list(map(itemgetter('name'), businesses)))
    review_count = (list(map(itemgetter('review_count'), businesses)))
    rating = (list(map(itemgetter('rating'), businesses)))
    price = [i.get('price') for i in businesses]
    location = [i.get('location') for i in businesses]
    phoneNum = [i.get('phone') for i in businesses]
    displayAdd = [i.get('display_address') for i in location]

    return name, review_count, rating, price, displayAdd, phoneNum

def database(name, review_count, rating, price, displayAdd, phoneNum):

    conn = sqlite3.connect('yelp.db')
    cur = conn.cursor() # used to issue sql commands

    cur.execute("DROP TABLE IF EXISTS MainDB")
    cur.execute('''CREATE TABLE MainDB(             
                       yid INTEGER NOT NULL PRIMARY KEY,
                       name TEXT,
                       rating REAL,
                       price TEXT,
                       total_reviews INTEGER,
                       address TEXT,
                       location INTEGER,
                       phone_number TEXT)''')
    cur.execute("DROP TABLE IF EXISTS LocationDB")
    cur.execute('''CREATE TABLE LocationDB(             
                       key INTEGER NOT NULL PRIMARY KEY,
                       cityState TEXT)''')
    ctr = 0
    for x in name:
        cur.execute('''INSERT INTO MainDB (name,rating,price,total_reviews,address, phone_number) VALUES (?,?,?,?,?,?)'''
                    ,(x,rating[ctr],price[ctr],review_count[ctr], displayAdd[ctr][0],phoneNum[ctr]))
        ctr += 1

    pk = 1
    for y in displayAdd:
        if y[-1] == 'Sunnyvale, CA 94087' or y[-1] == 'Sunnyvale, CA 94086' or y[-1] == 'Sunnyvale, CA 94085':
            cur.execute("UPDATE MainDB SET location = ? WHERE yid = ?",(1,pk))
        elif y[-1] == 'San Jose, CA 95129':
            cur.execute("UPDATE MainDB SET location = ? WHERE yid = ?",(2,pk))
        elif y[-1] == 'Cupertino, CA 95014' or y[-1] =='Cupertino, CA 95015':
            cur.execute("UPDATE MainDB SET location = ? WHERE yid = ?",(3,pk))
        elif y[-1] == 'Saratoga, CA 95070':
            cur.execute("UPDATE MainDB SET location = ? WHERE yid = ?",(4,pk))
        elif y[-1] == 'Mountain View, CA 94040':
            cur.execute("UPDATE MainDB SET location = ? WHERE yid = ?",(5,pk))
        elif y[-1] == 'Santa Clara, CA 95054' or y[-1] == 'Santa Clara, CA 95051':
            cur.execute("UPDATE MainDB SET location = ? WHERE yid = ?",(6,pk))
        pk += 1

    cur.execute('''INSERT INTO LocationDB (cityState) 
                   VALUES ('Sunnyvale'),('San Jose'), ('Cupertino'),('Saratoga'), 
                   ('Mountain View'),('Santa Clara')''')       

    conn.commit()
    conn.close()

def main():
    try:
        name, review_count, rating, price, displayAdd, phoneNum = request(API_HOST,SEARCH_PATH,API_KEY)
        database(name, review_count, rating,price, displayAdd,phoneNum)

    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )

if __name__ == '__main__':
    main()