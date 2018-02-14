# Gautam Mehta
# findwin.py
import os
import platform
import sys
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
        #startDir = os.path.expanduser("~")
        startDir = "/Users/gautammehta/Desktop/CIS40/"
        self.c = tk.StringVar()
        self.c.set(startDir)
        
        self.currentLabel = tk.Label(self, text= "Current folder: ")
        self.currentLabel.grid(row= 0, column=0, sticky= 'w')
        self.currentD = tk.Label(self, textvariable = self.c)
        self.currentD.grid(row = 0, padx=(100), sticky= "e")
        
        
        #Change button 
        changeButton= tk.Button(self, text = "Change Folder", command = lambda : self.__selectDir())
        changeButton.grid (row = 1, sticky = 'w')
        
        #Regex Filter label 
        regexLabel = tk.Label(self, text = "Regex Filter:")
        regexLabel.grid(row= 2, padx=(40), sticky = 'w')
        
        #Search Str label
        searchStrLabel = tk.Label(self, text = "Search String:")
        searchStrLabel.grid(row=3, padx=(40), sticky='w')
        
        #Entry box
        self.regexEntry = tk.StringVar() 
        self.searchEntry = tk.StringVar()
        entryBox1= tk.Entry(self, textvariable= self.regexEntry)
        entryBox2= tk.Entry(self, textvariable= self.searchEntry)
        
        entryBox1.grid(row= 2, column = 0, padx=(125))
        entryBox2.grid(row=3, column=0, padx=(155))
        
        entryBox1.bind("<Return>", self.__search)     
        entryBox1.focus_set()          
        entryBox2.bind("<Return>", self.__search) 
        
        #Listbox & scrollbar 
        s = tk.Scrollbar(self)   
               
        self.lbox = tk.Listbox(self, yscrollcommand=s.set)
        lboxTitle = tk.Label(self, text = "Results:")
        lboxTitle.grid(row=3, sticky = 'w', pady=(35,0))
        self.lbox.grid(row= 4,columnspan=2, sticky = 'we')
        
        s.config(command=self.lbox.yview)    
        s.grid(row=4,column=2, sticky='nse')
        
        #Label to show number of files  
        self.myCount = tk.StringVar()
        self.foundLabel = tk.Label(self, textvariable=self.myCount)
        self.foundLabel.grid(row=5, sticky= 'w')         
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(4,weight =1)
        
        self.fileList= []
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
        self.files.searchName(regex,self.searchEntry.get(),self.fileList)
        self.updateListBox()
        
    def updateListBox(self):
        if len(self.fileList) > 1000: 
            tkmb.showwarning(title="Overload!", message= str(len(self.fielList)) + ' files. There are too many files!', parent= self)
        else:
            self.lbox.insert(tk.END, *self.fileList)                    
            self.myCount.set("Found " + str(len(self.fileList)) + " files")
        
def main():
    win = FindWin()
    if platform.system() == 'Darwin': 
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is %d to true'
        os.system("/usr/bin/osascript -e '%s'" % (tmpl % os.getpid()))     
    win.mainloop()  
main()