'''
Created By Nixon Duong, Aiden Sun, Gautam Mehta, Chris Gentibano
Operating System : Mac OS
Complier/IDE : Wing/ IDLE
Date: 4-28-18 - > 4-29-18
Description: Using Googles street view API, we were able to grab images from 
             addresses from famous monuments located around the world. From the data retrieved, creates a game 
             that displays a random monument and allows the user to guess the monument. Points are awarded for every correct
             answer and stored on the score board.
'''
from tkinter import * #allows for Grapic user interface
import tkinter as tk
from ScoreBoardGui import * #imports the scoreboard class 
import sqlite3 #used for database 
import random #allows for a random integer to be generated

# links the monument to appropriate image 
class MonumentNode:
    def __init__(self,mi): # recieves a tuple parameter and sets self monument and image
        self.monument = mi[0]
        self.image = mi[1]
    def getMonument(self):   # returns the objs attribute monument 
        return (self.monument)
    def getImage(self): # returns the image
        return (self.image)


class GUI(tk.Tk):
    def __init__(self):
        super().__init__() 
        self.config(bg ='grey')
        self.title('CATCHA ALL')
        self.resizable(True, True)

        # LABEL OF THE GAME
        titleLabel = tk.Label(self,text='Catcha all')
        titleLabel.grid(row = 0, column = 0, columnspan=4, sticky='')
        titleLabel.config(bg='grey')

        #Photo Image Label
        base = "/Users/gautammehta/Desktop/CodingWeekend/"        
        conn = sqlite3.connect(base+'Monuments.db')
        cur = conn.cursor() # used to issue sql commands        
        fileList = [] #first list to grab tuples from DB
        cleanList = [] #cleaned up list to grab from tuple into string
        self.monumentList=[] # list of monument images in string
        cleanList2=[] 
        newL=[]
        self.high_score=0
        
        for i in cur.execute("SELECT Image FROM Monument") : # * means every single query in the database
            fileList.append(i) 
        for i in range(len(fileList)):
            cleanList.append(fileList[i][0])
        
        for i in cur.execute("SELECT Name FROM Monument") : # * means every single query in the database
            self.monumentList.append(i) 
        for i in range(len(self.monumentList)):
            cleanList2.append(self.monumentList[i][0]) 
            
        newL= list(zip(cleanList2,cleanList))
        
        self.monumentData = []
        for i in range (len(newL)):
            self.monumentData.append(MonumentNode(newL[i]))
            
        self.randList = []
        self.randList = self.randomGenerator() # random generator returns 4 random objects from the monumentData
        answerOffset = random.randint(0,3) # chooses a random answer out of the 4 
        self.answer = self.randList[answerOffset] # sets the answer to an monumentData obj
        
        #Photo Label
        base = "/Users/gautammehta/Desktop/CodingWeekend/"        
        img = PhotoImage(file = base+ self.answer.getImage())
        destination = tk.Label(self, image=img)
        destination.grid(row=1, column=0, columnspan=4)
        destination.image = img
        
        #Choice Buttons
        self.choice1 = tk.StringVar()
        self.choice1 = self.randList[0].getMonument()
        self.choiceB1 = tk.Button(self, text=self.choice1, command=lambda:self.check(self.choice1))
        self.choiceB1.grid(row=2, column=0, columnspan=2, sticky='')
        self.choiceB1.config(bg='grey')

        self.choice2 = tk.StringVar()
        self.choice2 = self.randList[1].getMonument()
        self.choiceB2 = tk.Button(self, text=self.choice2, command=lambda:self.check(self.choice2))
        self.choiceB2.grid(row=2, column=2, columnspan=2, sticky='')
        self.choiceB2.config(bg='grey')        
        
        self.choice3 = tk.StringVar()
        self.choice3 = self.randList[2].getMonument()
        self.choiceB3 = tk.Button(self, text=self.choice3, command=lambda:self.check(self.choice3))
        self.choiceB3.grid(row=3, column=0, columnspan=2, sticky='')
        self.choiceB3.config(bg='grey')
        
        self.choice4 = tk.StringVar()
        self.choice4 = self.randList[3].getMonument()
        self.choiceB4 = tk.Button(self, text=self.choice4, command=lambda:self.check(self.choice4))
        self.choiceB4.grid(row=3, column=2, columnspan=2, sticky='')
        self.choiceB4.config(bg='grey')        

        #Score Label
        scoreLabel = tk.Label(self, text='Score: ')
        scoreLabel.grid(row=4, column=0, sticky='sw')
        scoreLabel.config(bg='grey')
        
        #Counter Label
        self.counter = tk.IntVar()
        self.counter.set(0)
        counterLabel = tk.Label(self, textvariable=self.counter)
        counterLabel.grid(row=4, column=1, sticky='sw')
        counterLabel.config(bg='grey')

        #Scoreboard button
        scoreboardButton = tk.Button(self, text='ScoreBoard', command=self.openScoreboard)
        scoreboardButton.grid(row=4, column=2, sticky='e')
        scoreboardButton.config(bg='grey')

        #Give Up button
        giveUpButton = tk.Button(self, text='Give Up', command=self.terminate)
        giveUpButton.grid(row=4, column=3, sticky='e')
        giveUpButton.config(bg='grey')

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        
        # returns 4 random monumentData objects 
    def randomGenerator(self):
        randObj = []
        div = int(len(self.monumentData)/4)
        
        num1 = random.randint(0,div)
        randObj.append(self.monumentData[num1])
        
        num2 = random.randint(div+1,2*div)
        randObj.append(self.monumentData[num2])
        
        num3 = random.randint(2*div+1,3*div)
        randObj.append(self.monumentData[num3])
        
        num4 = random.randint(3*div+1,(4*div)-1)
        randObj.append(self.monumentData[num4])   
          
        return(randObj) 

    #appends the new scores onto the high_score .txt
    def save_high_score(self, new_high_score):
        try:
            base = "/Users/gautammehta/Desktop/CodingWeekend/"                    
            # Write the file to disk
            high_score_file = open(base+"high_score.txt", "a")
            high_score_file.write(str(new_high_score) + '\n')
            high_score_file.close()
        except IOError:
            print("Unable to save the high score.")
    
    #checks if the user won by comparing buttom pressed with the answer
    def check(self, args):
        #if correct, continue on displaying a new monument
        if str(self.answer.getMonument()) == str(args):
            counter = self.counter.get()
            counter+=100
            self.counter.set(counter)
            base = "/Users/gautammehta/Desktop/CodingWeekend/"                    
            self.randList = []
            self.randList = self.randomGenerator()
            answerOffset = random.randint(0,3)
            self.answer = self.randList[answerOffset]          
            
            self.choice1 = self.randList[0].getMonument()
            self.choice2 = self.randList[1].getMonument()
            self.choice3 = self.randList[2].getMonument()
            self.choice4 = self.randList[3].getMonument()
            
            img = PhotoImage(file = base+ self.answer.getImage())
            destination = tk.Label(self, image=img)
            destination.grid(row=1, column=0, columnspan=4)
            destination.image = img
            
            self.choiceB1.config(text=self.randList[0].getMonument())
            self.choiceB2.config(text=self.randList[1].getMonument())
            self.choiceB3.config(text=self.randList[2].getMonument())
            self.choiceB4.config(text=self.randList[3].getMonument())            
            
        else:
            # if incorrect button is pressed, terminates game and saves high score. Then displays the scoreboard
            self.save_high_score(self.counter.get())
            self.openScoreboard()
            self.terminate()
        
        #creates a scoreboard object which opens a new windew because the constructor does so
    def openScoreboard(self):
        scoreboard = scoreboardGUI()
    
        #ends the game by terminating self
    def terminate(self):
        self.destroy()

    #creates a GUI object which starts the game because the game is written in the constructor
def main() :
    win = GUI()
    win.mainloop() 
    
if __name__ == '__main__':
    main()