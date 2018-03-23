'''
Gautam Mehta
CIS 41A   Fall 2017
Unit G take-home assignment
''' 

"""
First Script
"""
def main():
    read_data_file()

def read_data_file():
    infile = open ("States.txt", "r")
    line = infile.readline()
    highest_population= -1
    for line in infile:
        fields = line.split(" ")
        stateInitials = fields[0]
        region= fields[1]
        population= int(fields[2])
        
        if region == "Midwest" and population > highest_population:
            highest_population = population
            print ("Highest population state in the Midwest is:", stateInitials, population)
    infile.close()
main()
'''
Execution Results:
Highest population state in the Midwest is: IL 12802000
'''

"""
Second Script
"""
list1 = [1,2,3]
try:
    print (list1[3])
except IndexError:
    print ("Error: bad index number.")
'''
Execution Results:
Error: bad index number.
'''

"""
Third Script
"""
class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}
class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}
class3 = {"Migel", "Zhang", "Hiroto", "Anita", "Jia"}

common = list(class1.intersection(class2).intersection(class3))
common.sort()
print("Students in all three classes:", common)

all_three = list(class1.union(class2).union(class3))
all_three.sort()
print("All students:", all_three)

half_and_half= list(class1.difference(class2,class3))
half_and_half.sort()
print("Students in class1 but not class2 or class3:", half_and_half)

'''
Execution Results:
Students in all three classes: ['Migel']
All students: ['Anita', 'Audry', 'Hiroto', 'Jia', 'Li', 'Migel', 'Sasha', 'Tanya', 'Zhang']
Students in class1 but not class2 or class3: ['Li']
'''