# Gautam Mehta
# filesearch.py
import os
import os.path
import re 
import cis41b.strsearch as ss

class FileSearch():
    def __init__(self,startDir):
        for (path, dirlist, filelist) in os.walk(startDir) :
            for f in filelist :
                self.myTuple= tuple((f,path))
    
    def searchName(self, regObj, searchStr, resList):
        resList = (self.myTuple for self.myTuple[0] in self.myTuple if (regObj.search(self.myTuple[0])) if (not searchStr or ss.strIsInFile()))
        print (resList)
        #resList= sorted(resList, key=lambda tup: tup[0])
        