#lab 4: system calls, package, GUI and regex review
# Gautam Mehta
import sys
import os
import platform
import re 
import tkinter as tk
import cis41b.findwin as findwin
import cis41b.filesearch as fs 


def usage():
    """ print Usage message if command line is invalid
        Valid format:  python  lab4.py   directory_path   regex
    """
    print("Usage:", end=' ')
    print("lab4.py <search directory> <regular expression filter>")

def main() :
    # if command line argument has only one word, instantiate the GUI window and run the mainloop
    if (len(sys.argv) == 1):
        win = findwin.FindWin()
        if platform.system() == 'Darwin': 
            tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is %d to true'
            os.system("/usr/bin/osascript -e '%s'" % (tmpl % os.getpid()))     
        win.mainloop()        
    # else if 3 words in command line argument,
    elif (len(sys.argv) == 3):
        # if the 2nd word is not a valid directory, print error message and return
        if not os.path.isdir(sys.argv[1]):
            print ("'%s' is not valid directory" % (sys.argv[1]))
            return
        # otherwise compile the regex in the 3rd word on the command line
        try :
            regex = re.compile(sys.argv[2],re.I)
                       
        except Exception as e :
            print("Invalid regex: " + str(e))
            return
        # run the search of the FileSearch object and print all the filenames
        for rs in fs.FileSearch(sys.argv[1]).searchName(regex):
            print (rs)
    else:
        usage()
main()
""" To set up the CIS41B package I created a package by creating a folder on my desktop called "CIS41B". 
Then I opened up Wing and created a new __init__.py file and saved that into my package directory. 
Lastly I added in the dialog.py, findwin.py, and filesearch.py files into the same package. Init file has
no code.
"""
