# lab 3: GUI with Tkinter, OOP
# Gautam Mehta
import tkinter as tk
import platform
import os
from dialog import Dialog
import tkinter.messagebox as tkmb

class AddStudentDialog (Dialog):
    def body(self, bodyFrame):
        self.entryID = tk.StringVar()
        self.entryName= tk.StringVar()
        self.entryLang= tk.StringVar()
        
        lId = tk.Label(bodyFrame, text= "Student ID: ")
        lId.grid(sticky='e')        
        tk.Entry(bodyFrame, textvariable=self.entryID).grid(row=0, column=1) 
        
        lName = tk.Label(bodyFrame, text= "Name: ")
        lName.grid(sticky ='e')        
        tk.Entry(bodyFrame, textvariable=self.entryName).grid(row=1, column=1) 
        
             
        lFavorite = tk.Label(bodyFrame, text= "Favorite Language: ")
        lFavorite.grid()    
        tk.Entry(bodyFrame, textvariable=self.entryLang).grid(row=2, column=1)        
        
        
    def validate(self):
        """Return True if all dialog options are valid"""
        if len(self.entryID.get()) == 0 or len(self.entryName.get()) == 0 or len(self.entryLang.get()) == 0:
            return False
        elif len(self.entryID.get()) > 3 or len(self.entryID.get()) < 3:
            return False
        elif self.entryLang.get().strip().lower() != "python":
            tkmb.showerror(title="Wow", message='I see how it is', parent= self)
            return True
        else:
            return True
        
    def apply(self):
        """set result to valid user input data"""       
        myDict = {"Student ID": self.entryID.get(), "Name": self.entryName.get(), "Favorite Language": self.entryLang.get()}
        self.result= myDict
    
class MainWindow (tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lab 3")
        self.resizable(True, False)   # horizontal only
        descLabel= tk.Label(self, text="Add a Student", fg="black")
        descLabel.grid(sticky='w')
        
        
        # creating a button to add student
        button = tk.Button(self, text="Click to Add", command= lambda: self.addStudent())
        button.grid(row=0, column= 1)
        
        # Listbox with scrollbar
        s = tk.Scrollbar(self) 
        self.lbox = tk.Listbox(self, height=3, yscrollcommand=s.set) 
        lboxTitle= tk.Label(self, text= "Student List", fg ="black")
        lboxTitle.grid(row= 0, column=2, sticky='we')
        self.lbox.grid(row=1, column= 2, sticky='we')
        
        self.grid_columnconfigure(2, weight=1)
        
        s.config(command=self.lbox.yview)    
        s.grid(row=1,column=3, sticky='nse')
        """UNABLE TO GET SCROLL BAR ON MAC UNTIL AFTER MORE THAN 3 STUDENTS BEEN ADDED"""
    def addStudent(self):
        data = AddStudentDialog(self)
        self.lbox.insert(tk.END, data.result)        
    
        studCountLabel = tk.StringVar()
        if self.lbox.size():  
            studCountLabel.set("Student Count = " + str(self.lbox.size()))
            studCountLabel = tk.Label(self, textvariable=studCountLabel)
            studCountLabel.grid(row=2, column=0)   
        
def main() :
    win = MainWindow()
    if platform.system() == 'Darwin': 
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is %d to true'
        os.system("/usr/bin/osascript -e '%s'" % (tmpl % os.getpid()))     
    win.mainloop()
main()