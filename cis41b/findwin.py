# Gautam Mehta
# findwin.py
import os
import os.path
import re 
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox as tkmb
import cis41b.filesearch as fs

class FindWin (tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FILE FINDER")
        self.currentD = tk.StringVar()
        startDir = os.path.expanduser("~")
        self.c = tk.StringVar()
        self.c.set(startDir)
        
        self.currentLabel = tk.Label(self, text= "Current folder: ")
        self.currentLabel.grid(row= 0, column=0, sticky= 'w')
        self.currentD = tk.Label(self, textvariable = self.c)
        self.currentD.grid(row = 0, padx=(100), sticky= "e")
        
        
        #Change button 
        changeButton= tk.Button(self, text = "Change Folder", command = lambda : self.__selectDir())
        changeButton.grid (row = 1, sticky = 'w')
        
        #Regex label 
        regexLabel = tk.Label(self, text = "Regex Filter:")
        regexLabel.grid(row= 2, padx=(40), sticky = 'w')
        
        #Entry box
        self.regexEntry = tk.StringVar() 
        entryBox= tk.Entry(self, textvariable= self.regexEntry)
        entryBox.grid(row= 2, column = 0, padx=(125))

        entryBox.bind("<Return>", self.__search)     
        entryBox.focus_set()          
        
        #Listbox & scrollbar 
        s = tk.Scrollbar(self)   
               
        self.lbox = tk.Listbox(self, yscrollcommand=s.set)
        lboxTitle = tk.Label(self, text = "Results:")
        lboxTitle.grid(row=2, sticky = 'w', pady=(35,0))
        self.lbox.grid(row= 3,columnspan=2, sticky = 'we')
        
        s.config(command=self.lbox.yview)    
        s.grid(row=3,column=2, sticky='nse')
        
        #Label to show number of files  
        self.myCount = tk.StringVar()
        self.foundLabel = tk.Label(self, textvariable=self.myCount)
        self.foundLabel.grid(row=4, sticky= 'w')         
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(3,weight =1)
        self.update() 
        
        self.files = fs.FileSearch(startDir)
        
        
    def __selectDir(self):
        startDir = tk.filedialog.askdirectory(initialdir= self.c.get(), title= "Select Start Directory") 
        if startDir:
            self.c.set(startDir)
            self.files = fs.FileSearch(startDir)
            self.__search
        
    def __search(self,*args):
        try :
            user_input = '{}'.format(self.regexEntry.get())
            regex = re.compile(user_input, re.I)
        except Exception as e:
            tkmb.showerror(title="Wrong!", message='Please enter a valid regex', parent= self)
            return 
        self.lbox.delete(0,tk.END)
        fileList = self.files.searchName(regex)
        if len(fileList) > 1000: 
            tkmb.showwarning(title="Overload!", message= str(len(fileList)) + ' files. There are too many files!', parent= self)
        else:
            self.lbox.insert(tk.END, *fileList)                    
            self.myCount.set("Found " + str(len(fileList)) + " files")
        