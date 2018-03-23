'''
Gautam Mehta
In class unit C
'''
import re
string = " "
while string != "Q":
    string = input("Enter regular expression: ")
    if re.search(r"^[aeiou]", string):
        print (string + " starts with a vowel\n")
    else:
        print (string + " does not start with a vowel\n")
