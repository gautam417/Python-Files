"""
Gautam Mehta
CIS 41A Fall 2017
ICE_G
"""
'''
Part 1
'''
myfile = open ("ZenOfPython.txt", "a+")
myfile.write("Beautiful is better than ugly.\n")
myfile.write("Explicit is better than implicit.\n")
myfile.close()

myfile = open("ZenOfPython.txt", "a+")
myfile.write("Readability counts.\n")
myfile.write("If the implementation is hard to explain, it's a bad idea.")
myfile.close()

myfile= open("ZenOfPython.txt", "r")
x= myfile.read() 
print (x)
myfile.close()

"""
Execution Results:
Beautiful is better than ugly.
Explicit is better than implicit.
Readability counts.
If the implementation is hard to explain, it's a bad idea.
"""
'''
Part 2
'''
class1= set(["Li", "Audry", "Jia", "Migel", "Tanya"])
class2= set(["Sasha", "Migel", "Tanya", "Hiroto", "Audry"])

class1.add("John")
common = list(class1.intersection(class2))
common.sort()
print("Students in both classes:", common)

both = list(class1.union(class2))
both.sort()
print("All students:", both)

if "Sasha" in class1:
    print("Sasha is in class1")
else:
    print("Sasha is not in class1")

"""
Execution Results:
Students in both classes: ['Audry', 'Migel', 'Tanya']
All students: ['Audry', 'Hiroto', 'Jia', 'John', 'Li', 'Migel', 'Sasha', 'Tanya']
Sasha is not in class1
"""