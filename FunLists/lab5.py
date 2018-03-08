"""
Gautam Mehta
Output:
The smallest number in [5, 8, 100, 1, 5, -2] is -2
The largest number in [5, 8, 100, 1, 5, -2] is 100
Sum of all numbers in [5, 8, 100, 1, 5, -2] is 117
Enter the number to find in the list and also count occurences of: 5
5 was found at index 0 of [5, 8, 100, 1, 5, -2]
5 occurs 2 times in [5, 8, 100, 1, 5, -2]

The smallest number in [5, 8, 100, 1, 5, -2] is -2
The largest number in [5, 8, 100, 1, 5, -2] is 100
Sum of all numbers in [5, 8, 100, 1, 5, -2] is 117
Enter the number to find in the list and also count occurences of: 1000000
1000000 was not found at all in [5, 8, 100, 1, 5, -2]
"""
import sys
#Lab 5
myList =[5, 8,100,1,5,-2]

#minimum 
minimum = myList[0]
for i in myList:
    if minimum > i:
        minimum = i
print ("The smallest number in", myList, "is", minimum)

#maximum
maximum = myList[0]
for i in myList:
    if maximum < i:
        maximum = i
print ("The largest number in", myList, "is", maximum)

#sum
total=0
for i in myList:
    total +=i
print ("Sum of all numbers in", myList, "is", total)

#Find number 
count = 0
list2=[]
search = int(input("Enter the number to find in the list and also count occurences of: "))
if search not in myList:
    print (search, "was not found at all in", myList)
    sys.exit()
for i,x in enumerate(myList):
    if x == search:
        list2.append(i)
        count+=1
print (search, "was found at index", list2[0],"of", myList)
print (search, "occurs", count, "times in", myList)


