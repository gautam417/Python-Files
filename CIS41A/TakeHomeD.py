'''
Gautam Mehta
CIS 41A Fall 2017
Unit D take-home assignment
'''
"""
First Script
"""
num = int(input("Please enter the number of rows: "))
for x in range (1,num+1):
    for y in range (1, x+1):
        if y <= x:
            print (str(y*x).rjust(1), end = ' ')
    print ()
    
"""
Second Script
"""
import random

average = 0
highscore = 0
runs= 10000
for i in range (0, runs):
    money_won= 0
    roll = random.randint(1,6)
    while roll > 3:
        if roll == 4:
            money_won+=4
            average+=4
        elif roll == 5:
            money_won+=5
            average+=5
        elif roll== 6:
            money_won+=6
            average+=6
        roll = random.randint(1,6)
    if highscore <money_won:
        highscore=money_won
    money_won= 0
avg=str(average/runs)
print("The average is: "+avg)
print("The Highest score is: "+str(highscore))

"""
Third Script
"""       

import re
string = "Beautiful is better than ugly - The Zen of Python"
search= re.findall(r"\b\w*?([aeiouAEIOU])", string)
joined =",".join(search)
print (joined)


"""
Fourth Script
"""
import re
string = "The rabbit, the onion, the garlic, the tomato, some salt, stew and then we have the feast."
string= re.sub("the ", "a ", string)
string2= re.sub("The ", "A ", string)
print (string2)

"""
Execution Results:
Please enter the number of rows: 12
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
9 18 27 36 45 54 63 72 81 
10 20 30 40 50 60 70 80 90 100 
11 22 33 44 55 66 77 88 99 110 121 
12 24 36 48 60 72 84 96 108 120 132 144 
The average is: 5.0962
The Highest score is: 77
e,i,e,a,u,e,e,o,o
A rabbit, a onion, a garlic, a tomato, some salt, stew and then we have a feast.
"""
