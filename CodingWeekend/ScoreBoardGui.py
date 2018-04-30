from tkinter import*
import tkinter as tk



class scoreboardGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg = 'white')
        self.title('Score Board')
        self.resizable(True,True)
        
        #Scoreboard Label
        titleLabel = tk.Label(self,text='Scoreboard')
        titleLabel.grid(row=0, column=0, columnspan=2, sticky='')
        
        #Listbox and Scrollbar       
        scrollbar = tk.Scrollbar(self)
        self.resultListbox = tk.Listbox(self, yscrollcommand=scrollbar.set)
        self.resultListbox.grid(row=1, columnspan=2, sticky='nesw')
        scrollbar.config(command=self.resultListbox.yview)
        scrollbar.grid(row=1, column=2, sticky='nes')
        
        #Updating Score and inserting to Listbox
        total_rankings = self.get_high_score()
        total_rankings = sorted(total_rankings, key = int, reverse=True)
        
        for item in total_rankings:
            self.resultListbox.insert(tk.END, item)        

        #Resizable Scale
        self.grid_columnconfigure(1, weight=1) 
        self.grid_rowconfigure(1, weight=1)
    
    def get_high_score(self):     
        # Try to read the high score from a file
        try:
            base = "/Users/gautammehta/Desktop/CodingWeekend/"
            with open(base+'high_score.txt') as f:
                content = f.readlines()
            
            content = [x.strip() for x in content]
        except IOError:
            # Error reading file, no high score
            print("There is no high score yet.")
        except ValueError:
            # There's a file there, but we don't understand the number.
            print("I'm confused. Starting with no high score.")
     
        return content