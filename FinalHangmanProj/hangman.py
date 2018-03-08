#Gautam Mehta
"""
Output:
Output for <secret word money>:

Welcome to Hangman!

_ _ _ _ _ ( 6 error-attempts left)

Guess a letter: k

There is no k

_ _ _ _ _ ( 5 error-attempts left)

Guess a letter: o

_ o _ _ _ ( 5 error-attempts left)

Guess a letter: m

m o _ _ _ ( 5 error-attempts left)

Guess a letter: a

There is no a

m o _ _ _ ( 4 error-attempts left)

Guess a letter: n

m o n _ _ ( 4 error-attempts left)

Guess a letter: e

m o n e _ ( 4 error-attempts left)

Guess a letter: y

m o n e y ( 4 error-attempts left)

m o n e y (you got it after picking 7 letters)
"""
import turtle
import time
from random import randint
import sys
screen = turtle.Screen()  
    
class drawing(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.hideturtle()
  
gallow = drawing()
hangman = drawing()
hangman.right(90)

def drawgallow():
    screen.tracer(0)
    gallow.reset()
    gallow.hideturtle()
    gallow.penup()
    gallow.goto(-150,180)
    gallow.pendown()
    gallow.forward(55)
    gallow.penup()
    gallow.goto(-150,180)
    gallow.right(90)
    gallow.pendown()
    gallow.forward(150)
    gallow.penup()
    gallow.goto(-180, 30)
    gallow.pendown()
    gallow.left(90)
    gallow.forward(60)
    gallow.penup()
    gallow.goto(-95, 180)
    gallow.right(90)
    gallow.pendown()
    gallow.forward(20)
    gallow.penup()
    screen.tracer(1)

def drawhead():
    hangman.goto(-105,151)
    hangman.pendown()
    hangman.circle(10)
    hangman.penup()

def drawbody():
    hangman.goto(-95, 141)
    hangman.pendown()
    hangman.forward(51)
    hangman.penup()

def drawlimb(part):
    # draw left arm
    if part == 'larm':
        hangman.goto(-95, 130)
        hangman.pendown()
        hangman.goto(-108, 100)
        hangman.penup()
    # draw right arm
    elif part == 'rarm':
        hangman.goto(-95, 130)
        hangman.pendown()
        hangman.goto(-82, 100)
        hangman.penup()
    # draw left leg
    elif part == 'lleg':
        hangman.goto(-95, 90)
        hangman.pendown()
        hangman.goto(-108, 60)
        hangman.penup()
    # draw right leg  
    elif part == 'rleg':
        hangman.goto(-95, 90)
        hangman.pendown()
        hangman.goto(-82, 60)
        hangman.penup()

def wholebody():
    drawhead() # 1st wrong guess
    drawbody() #2nd wrong guess 
    drawlimb('larm') #3rd wrong guess 
    drawlimb('rarm') #4th wrong guess 
    drawlimb('lleg') # 5th wrong guess 
    drawlimb('rleg') #6th wrong guess
    
word_list=[]
try:
    fin = open('words.txt') #open words file
    for line in fin:
        word = line.lower().strip() #take away trailing newline chars and make them all lowercase
        word_list.append(word)
    fin.close()
except:
    print("Could not open file, something went wrong.")

r = randint(1, len(word_list))
secret_word = word_list[r-1]
print ("Output for <secret word "+secret_word+">:\n")
print ("Welcome to Hangman!\n")
drawgallow()

display =[]
for i in secret_word:
    display.append('_')
attempts = 6
count = 0
print(" ".join(display),end='')
print(" (",attempts,"error-attempts left)")
while attempts != 0:
    guess = input("\nGuess a letter: ")
    if guess in display:
        print("\nYou have already entered in this guess. I will not penalize you.\n")
        print(" ".join(display),end='')
        print(" (",attempts,"error-attempts left)")
        
    elif guess in secret_word:
        indices = [i for i,x in enumerate (secret_word) if x == guess]
        for i in indices:
            display[i]=guess
        print()
        print(" ".join(display),end='')
        print(" (",attempts,"error-attempts left)")
        
    else:
        print("\nThere is no", guess)
        print()
        attempts-=1
        print(" ".join(display),end='')
        print(" (",attempts,"error-attempts left)")
    
    count+=1
    if (all(i[:] != '_' for i in display)) == True:
        print()
        print(" ".join(display),end='')
        print(" (you got it after picking", count, "letters)")
        turtle.exitonclick()
        break
    
    if attempts == 0:
        print("\nThe secret word was "+ secret_word+". Good luck next time.")
        drawlimb('rleg')
        wholebody()
        turtle.exitonclick()
        
    elif attempts == 1:
        drawlimb('lleg')
        
    elif attempts == 2:
        drawlimb('rarm')
                
    elif attempts == 3:
        drawlimb('larm')
                
    elif attempts == 4:    
        drawbody()
            
    elif attempts == 5:
        drawhead()
                
        
