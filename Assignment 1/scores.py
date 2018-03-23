#Gautam Mehta
class Scores:
    def __init__(self): #constructor that reads in line by line of the input file and stores data in self
        try:
            myFile = open("input.txt", "r") 
            self.data = tuple((line.split()) for line in myFile)
            self.keys=self.data[0]
            self.dictionary ={}
        except IOError: 
            print ("File could not open. Please try again!")
            
    def getOne(self):
        scores = []
        for i in range(len(self.keys)):
            self.values= list((line[i]) for line in self.data)
            self.scores= self.values[1:]
            self.dictionary[self.keys[i]]= self.scores
        self.keys = sorted(self.keys)
        i=0
        while i <len(self.dictionary):
            yield self.keys[i], self.dictionary[self.keys[i]]
            i+=1
    def printByLast(self):
        for k,v in sorted(self.dictionary.items(),key=lambda r : r[1][-1], reverse=True):
            print (k,":",*v)
    def printMaxMin(self):
        scoresDict= {key :sum(list(map(float,value))) for key, value in self.dictionary.items()}
        
        orderedList = sorted(scoresDict.items(), key=lambda r:r[1], reverse=True)
        print ("max total:", orderedList[0][1])
        print ("min total:", orderedList[-1][1])
        
                
        
        