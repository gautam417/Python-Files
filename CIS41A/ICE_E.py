"""
Gautam Mehta
CIS 41A Fall 2017
ICE_E
"""
import random
def welcome():
    print("Welcome to the dice rolling game")
def rollDie(sides =6):
    return int(random.randint(1,sides))
def playGame(runs):
    money_won= 0
    average = 0
    highscore = 0
    for i in range (0, runs):
        die = rollDie()
        while die > 3:
            if die == 4:
                money_won+=4
                average+=4
            elif die == 5:
                money_won+=5
                average+=5
            elif die== 6:
                money_won+=6
                average+=6
            die= rollDie()
        if highscore <money_won:
            highscore=money_won
            
        money_won= 0
    avg=str(average/runs)
    print("The avg is: "+avg)
    print("The Highest score is: "+str(highscore))

def main():
    welcome()
    playGame(10000)
main()

import copy
def funWithLists():
    list1=[2,4,6]
    list2=list1
    list3= copy.deepcopy(list1)
    list1.append(8)
    list2.insert(1,3)   
    list3.pop(0)
    
    print ("List 1:", list1)
    print ("List 2:", list2)
    print ("List 3:", list3)
funWithLists()