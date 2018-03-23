# CIS 41B
# Dialog window base class

import tkinter as tk
from abc import ABC, abstractmethod     # abstract base class is a class to derive other classes from 
                                        # the abstract class is never supposed to be instantiated 
                                        
# inheriting from both tk and abstract class 
# you can have multiple inheritance as long as different classes 

class Dialog(tk.Toplevel, ABC):    # Multiple inheritance: Dialog gets the attributes of TopLevel and ABC
    """Base Dialog() class
       - Has standard features of a dialog box: 
          - a window with [OK] and [Cancel] buttons
          - [OK] to commit a transaction, [Cancel] to cancel a transaction
       - Derived dialog boxes can be created with a small amount of customization"""
    # this is called doc string^
# topLevel window doesnt inherit from the tk class, it inherits from toplevel class
# master will always be second arg so that toplevel and tk will connect and coordinate
# kwargs allows u to use widgets, buttons, whatever u want 
    def __init__(self, master, title=None, **kwargs):    # Q1. what is kwargs and why would this base class want to use it?
                                                         # A1. kwagrs means keyworded variable arguments and it means that
                                                         # it can accept multiple arguments that have their variables defined
                                                         # from the call. It is useful to have this in the base class so that
                                                         # the child class will be able to create widgets,buttons, etc.
                                                         # to make their code more functional.

        """ set up window with title, body, [OK] and [Cancel] buttons, and controls"""
        # the ABC class 
        # to overwrite both classes we need to use the __init__ method
        ABC.__init__(self)
        tk.Toplevel.__init__(self, master)  # self is Dialog, 
                                            # master is window that Dialog is spawned from, which in lab 3 is MainWindow
                                            # master needs to be passed in so that if master closes, then all spawned windows will go away
                                            # master is not tk.toplevel
        self.grab_set()                                 # Make Dialog modal (Dialog grabs all focus, master is not active)
        self.protocol("WM_DELETE_WINDOW", self.cancel)  # Make "X" same as [Cancel] button, cancel is callback function
                                                        # the dialong window is now grabbing focus, not mainWindow  
        self._master = master           # save master window for this Dialog instance
        self.result = None              # result is *public* data that can be accessed outside the class.
                                        # result has the user input that is the result of the dialog with the user
                                        # you can say dialog.result and get the result that the user entered
                                        # take the three pieces of info and store into self.result 
                                        # you can say something like print(mywin.result)
                                        # there has to be some type of public variable before the user hits X (to store data)
        if title:
            self.title(title)           # Q2. What does this if statement do?
                                        # A2. This if statement says that if the user of this base class 
                                        # creates a title, then store that title in self.title

        self.v = tk.StringVar()         # Provide a generic StringVar v that can be used to store user input data for the transaction
                                        # the StringVar stores the result. We will not be using StringVar
                                        # its generic for simple windows
        self.v.set('ERROR: uninitialized data')    # if a derived class wants to use v, it must set v

        bodyFrame = tk.Frame(self)                      # Create empty body frame for derived class to fill
                                                        # frame is another widget, putting things in a frame is common to build windows 
        self.initial_focus = self.body(bodyFrame)       # Call the body() method to populate the window's body.
                                                # The body method will return a widget, and the focus will be on the returned widget.
                                                # Having a focus on a widget means the cursor will be at that widget.
        
        # using pack to not be flexible on purpose                                                    
        bodyFrame.pack(padx=5, pady=5, fill=tk.BOTH, expand='y')  

        self.buttonbox()                        # create [OK] and [Cancel] buttons as another frame (two buttons)

        if not self.initial_focus:              # if focus is not on a widget, then focus is Dialog 
            self.initial_focus = self
        self.initial_focus.focus_set()          # set the focus
        
        # Q3. Explain where the focus could be. There are 3 possibilities, with a certain precedence: first, second, third
        # List the 3 locations in order. 
        # A3. First: Dialog 
        #     Second: Frame widget (bodyFrame)
        #     Third: Cancel
        
        # the two windows have to talk together, if someone hits minimize, then both windows will go away 
        self.transient(master)      # Set Dialog to be transient to the master:
                                    # This means: 1. Dialog will minimize if master is minimized 
                                    # 2. Dialog causes no extra icon on taskbar
                                    # 3. Dialog appears on top of master

        self.geometry("+%d+%d" % (master.winfo_rootx()+50, master.winfo_rooty()+50)) # place Dialog window on right and down from master
        self.resizable(False,False) # Don't allow Dialog to be sizeable

        self.wait_window(self)      # Stay open until Dialog is closed by the user
    #
    #=====  methods for appearance and behavior of Dialog  =====
    #
    # my job is to override it to instantiate my own class 
    @abstractmethod
    def body(self, bodyFrame):
        """Create dialog body.  Return widget that should have initial focus."""
        raise NotImplementedError

    def buttonbox(self):
        """Add [Ok] and [Cancel] buttons]"""
        box = tk.Frame(self) # example of how to add a frame 
        # the box is the master of the buttons
        self.b_ok = tk.Button(box, text="OK", width=10, command=self.ok) 
        self.b_ok.pack(side=tk.LEFT, padx=5, pady=5)
        self.b_cancel = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        self.b_cancel.pack(side=tk.LEFT, padx=5, pady=5)

        if not self.initial_focus:
            self.initial_focus = self.b_cancel
        
        self.bind("<Return>", self.return_)        # bind() method connects a pressed key event
        self.bind("<Escape>", self.cancel)         # to a method through a callback

        box.pack()
        
    @abstractmethod
    # i have to write the validate method 
    def validate(self):
        """Return True if all dialog options are valid"""
        raise NotImplementedError        
    # ok is a call back function 
    def ok(self, *args):
        """[Ok] button to commit change"""
        if not self.validate():                     # if not valid(true) the forcefully
            self.initial_focus.focus_set()          # put focus back to initial focus
            return

        self.apply()                # if everything is valid (true), then store input data into result
        self.cancel()               # go to close window

    def cancel(self, *args):
        """[Cancel] button to close window"""
        self._master.focus_set()    # set focus back to the master window
        self.destroy()              # close window

    def return_(self, *args):
        """Hitting return will run the button that has focus"""
        if self.focus_get() == self.b_cancel:
            self.cancel()
        elif self.focus_get() == self.b_ok:
            self.ok()
    def apply(self):
        """set result to valid user input data"""
        self.result = self.v.get()   # result defaults to the generic StringVar v variable
                                     # If derived class handles multiple data in a data structure
                                     # then the derive class should override this method so result
                                     # can be a data structure.
                                     # take what you got from user input and store to self.result ( )
                                     # v is a generic string var, so need to replace with a dictionary 

# Q4. Name all the callback methods
# A4. # self.b_cancel = tk.Button(box, text="Cancel", width=10, command=self.cancel)
      # self.b_ok = tk.Button(box, text="OK", width=10, command=self.ok) 
      # self.bind("<Return>", self.return_) 
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

