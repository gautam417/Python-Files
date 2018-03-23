'''
Gautam Mehta
CIS 41A   Fall 2017
Unit C take-home assignment
'''

'''
Part 1
1)
(r"a$", string)
2)
(r"a{2,4}", string)
3)
(r"a|b", string)
4)
(r"[^ab]+", string)
5)
(r"abc", string)
6)
(r"\w\s\d", string)
7)
(r"[\.]+", string)
8)
(r"\w", string)
'''

'''
Part 2
First Script
'''
string = "Believe you can and you're halfway there."
string2 = "a" 
num= string.count(string2)
index = 0
count = 0
while count <num:
    count+=1
    index=string.find(string2,index+1)
    print (index)
'''
Second Script
'''
num=0
while num>10 or num<20:
    num= int(input("Enter a number between 10 and 20: "))
    if (num >20) or (num <10):
        print ("Error! Please enter a number between 10 and 20: ")
    else:
        print("Congrats, This number is between 10 and 20.")
        break
'''
Third Script
'''
import re
data = 0
while data != "Q":
    data=input("Enter data from the keyboard: ")
    if re.search(r"^\d",data):
        print (data)

'''
Execution Results:
13
16
28
32
Enter a number between 10 and 20: 6
Error! Please enter a number between 10 and 20: 
Enter a number between 10 and 20: 26
Error! Please enter a number between 10 and 20: 
Enter a number between 10 and 20: 16
Congrats, This number is between 10 and 20.
Enter data from the keyboard: 29 palms
29 palms
Enter data from the keyboard: b52s
Enter data from the keyboard: 42
42
Enter data from the keyboard: Q
'''