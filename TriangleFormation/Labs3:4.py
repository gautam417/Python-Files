# Gautam Mehta
# Labs 3&4 
# CIS 40
from random import randint

def triangleType(a,b,c):
    if (a >= b + c) or (b >= a + c) or (c >= a + b):
        print ("A triangle cannot be formed with lengths",a,b,c)
    elif a==b and b==c and a==c:
        print ("An equilateral triangle will be formed with lengths", a,b,c)
    elif a!=b !=c:
        print ("A scalene triangle will be formed with lengths",a,b,c)
    else:
        print ("An isoceles triangle will be formed with lengths", a,b,c)   
       
def automation():
    a = randint(1,6)
    b = randint(1,6)
    c = randint(1,6)
    print("Randomly generated sides are:",a,b,c)
    triangleType(a,b,c) 
    
def repeat(a,b,c):
    a,b,c= (map(int,input("Enter the length of all three sides seperated by spaces: ").split(" ")))
    triangleType(a,b,c)                        
        
def main():
    a = 0
    b = 0
    c = 0        
    repeat(a,b,c)
    done = False    
    while not done:   
        answer = (input("Would you like to try again? Choose from [repeat, automate, quit]:"))   
        if answer == 'quit':
            print ("bye")
            done = True
        elif answer == "automate":
            automation()  
        elif answer == "repeat":
            repeat(a,b,c)
main()
