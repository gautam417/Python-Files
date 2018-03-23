'''
Gautam Mehta
CIS 41A Fall 2017
Unit E take-home assignment
'''

"""
First Script
"""

def invoice(unitPrice, quantity, shipping = 10, handling = 5):
    print ("Cost:",unitPrice*quantity)
    print ("Shipping:",shipping)
    print ("Handling:",handling)
    total = (unitPrice*quantity)+shipping+handling
    print ("Total:",total)
def main ():
    invoice(20,4,shipping =8)
    invoice(15,3,handling=15)
main()

'''
Execution results:
Cost: 80
Shipping: 8
Handling: 5
Total: 93
Cost: 45
Shipping: 10
Handling: 15
Total: 70
'''
print ("\n")
"""
Second Script
"""
def uniqueList():
    import random
    list1 = []
    
    
    while len(list1)!= 10:
        x= random.randint(1,15)
        if x not in list1:
            list1.append(x)
        else:
            x= random.randint(1,15)
    print (list1)
    sum_List1= sum(list1)
    print ("Sum =", sum_List1)
def main ():
    uniqueList()
main()
'''
Execution results:
[7, 9, 6, 2, 5, 8, 1, 14, 10, 4]
Sum = 66
'''
print ("\n")
"""
Third Script
"""
def rangeList():
    import random
    list2= list(range(50,61,2))
    random.shuffle(list2)
    print (list2)
    if list2[0]<53:
        print ("Index of first list element less than 53 is:", 0)
    elif list2[1]<53:
        print ("Index of first list element less than 53 is:", 1)
    elif list2[2]<53:
        print ("Index of first list element less than 53 is:", 2)  
    elif list2[3]<53:
        print ("Index of first list element less than 53 is:", 3) 
    elif list2[4]<53:
        print ("Index of first list element less than 53 is:", 4)
    elif list2[5]<53:
        print ("Index of first list element less than 53 is:", 5)    
def main():
    rangeList()
main()
'''
Execution results:
[52, 60, 58, 56, 54, 50]
Index of first list element less than 53 is: 0
'''
print ("\n")
"""
Fourth Script
"""
def sliceList():
    list3= list(range(1,11))
    sliced_list = list3[4:7]
    for i in range(len(sliced_list)):
        print(sliced_list[i])    
def main():
    sliceList()
main()
'''
Execution results:
5
6
7
'''
print ("\n")
"""
Fifth Script
"""
import random
def diceTest():
    rollResults= [0,0,0,0,0,0,0,0,0,0,0,0,0]
    count = 0
    while count <100000:
        dice1= random.randint(1,6)
        dice2= random.randint(1,6)
        total= dice1+dice2
        rollResults[total] +=1
        count+=1
    print("Chance of rolling 0: "+str(round((rollResults[0]/1000), 2))+"%")
    print("Chance of rolling 1: "+str(round((rollResults[1]/1000),2))+"%")
    print("Chance of rolling 2: "+str(round((rollResults[2]/1000),2))+"%")
    print("Chance of rolling 3: "+str(round((rollResults[3]/1000),2))+"%")
    print("Chance of rolling 4: "+str(round((rollResults[4]/1000),2))+"%")
    print("Chance of rolling 5: "+str(round((rollResults[5]/1000),2))+"%")
    print("Chance of rolling 6: "+str(round((rollResults[6]/1000),2))+"%")
    print("Chance of rolling 7: "+str(round((rollResults[7]/1000),2))+"%")
    print("Chance of rolling 8: "+str(round((rollResults[8]/1000),2))+"%")
    print("Chance of rolling 9: "+str(round((rollResults[9]/1000),2))+"%")
    print("Chance of rolling 10: "+str(round((rollResults[10]/1000),2))+"%")
    print("Chance of rolling 11: "+str(round((rollResults[11]/1000),2))+"%")
    print("Chance of rolling 12: "+str(round((rollResults[12]/1000),2))+"%")

def main():
    diceTest()
main()
'''
Execution results:
Chance of rolling 0: 0.0%
Chance of rolling 1: 0.0%
Chance of rolling 2: 2.77%
Chance of rolling 3: 5.62%
Chance of rolling 4: 8.19%
Chance of rolling 5: 11.09%
Chance of rolling 6: 14.12%
Chance of rolling 7: 16.37%
Chance of rolling 8: 14.02%
Chance of rolling 9: 11.15%
Chance of rolling 10: 8.38%
Chance of rolling 11: 5.55%
Chance of rolling 12: 2.74%
'''