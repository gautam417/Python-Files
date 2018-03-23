'''
Gautam Mehta
CIS 41A   Fall 2017
Unit F take-home assignment
'''
"""
Script 1
"""
list1 = [1,2,3]
list2 = [4,5,6]
def swaplist(x,y):
    list1[0],list2[0]= list2[0],list1[0]
def main():
    swaplist(list1,list2)
    print (list1)
    print (list2)
main()
'''
Execution results:
[4, 2, 3]
[1, 5, 6]
'''

"""
Script 2
"""


def main():
    printGroupMembers("Group A", "Li", "Audry", "Jia")
    print()
    groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"] 
    printGroupMembers(*groupB)
def printGroupMembers(gName, *sNames):
    print ("Members of", gName)
    for x in sNames:
        print (x)     
main()
'''
Execution results:
Members of Group A
Li
Audry
Jia

Members of Group B
Sasha
Migel
Tanya
Hiroto
'''

"""
Script 3
"""
print ("\n")

import math

def listComp():
    yearNumber = [1,2,3,4,5,6]
    changedList= [round(1000.0 *math.e**(0.05*y), 2) for y in yearNumber]
    
    print(changedList)
    
def main():
    listComp()
main()

'''
Execution results:
[1051.27, 1105.17, 1161.83, 1221.4, 1284.03, 1349.86]
'''