"""
Gautam Mehta
ICE_I
"""
print("Part 1")
class StateData: 
    name=""
    def __init__(self,name,abbreviation,region, population):    
        self.name = name
        self.abbreviation = abbreviation
        self.region = region
        self.population = int(population)
    def __str__ (self):
        return self.name 
    def displayState(self):
        print (self.name+ " (" + self.abbreviation +") "+ "is in the " + self.region + " region and has population of " + str(self.population))

s1 = StateData("California","CA", "West", 39250000)
print(s1)
s1.displayState()

print("\n")

print("Part 2")
class StateData2:
    def __init__(self,name):
        self.name = name
    def setRegion(self, region):
        self.region = region
    def getRegion(self):
        return self.region
s2= StateData2("California")
s2.setRegion("West")
s2.pop = 39250000

print (s2.name)
print (s2.getRegion())
print (s2.region)
print (s2.pop)
print ("\n")

print ("Part 3")
class StateData2:
    def __init__(self):
        self.public= "Public"
        self._protected= "Protected"
        self.__private= "Private"
test = StateData2()
print (test.public)
print (test._protected)
print (test.__private)