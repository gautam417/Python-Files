"""
Gautam Mehta
CIS 41A Fall 2017
ICE_F
"""
myInt=3
myList= [0,1,2]

def byVal(y):
    print ("Original ID of parameter in byVal is:", id(y))
    x= y+7
    print ("ID of parameter in byVal after change is:", id(x))
def byRef(b):
    print("Original ID of parameter in byRef is:",id(b))
    w=len(b)-1
    print("Original ID of parameter's last element in byRef is:",id(w))
    b[len(b)-1]+=7
    print("ID of parameter in byRef after change:", id(b))
    
def main():
    print("Original ID of myInt in main is:",id(myInt))
    print("Original ID of myList in main is:", id(myList))
    print("ID of myList's last element in main is:", id(len(myList)-1))
    
    byVal(myInt)
    byRef(myList)
    
    print("ID of parameter's last element in byRef after change:", id(myInt))
    print ("ID of myList in main after call to byRef is:", id(myList))
    print ("ID of myList's last element in main after call to byRef is:", id(len(myList)-1))
    print("myInt is now:", myInt)
    print("myList is now:", myList)
main()

'''
Part 2
Ragged Table
'''
def build_bell(num_rows):
    rtable = [[1]]
    
    for i in range(1, num_rows):
        rtable.append([rtable[i - 1][-1]])
        
        for j in rtable[i - 1]:
            rtable[i].append(rtable[i][-1] + j) 
    return rtable

def print_bell(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            num = str(table[i][j])
            print(num.rjust(4), end = ' ')
        print("")

def main():
    print_bell(build_bell(6))

main()

