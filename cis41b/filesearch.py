# Gautam Mehta
# filesearch.py
import os
import os.path
import re 
from collections import defaultdict
class FileSearch():
    def __init__(self,startDir):
        self.myDict = defaultdict(list)
        for (path, dirlist, filelist) in os.walk(startDir) :
            for f in filelist :
                self.myDict[f].append(os.path.join(path,f))
    def searchName(self, regObj):
        self.result = (rs for rs in self.myDict if regObj.search(rs))
        return sorted(p for rs in self.result for p in self.myDict[rs])
    
    

    