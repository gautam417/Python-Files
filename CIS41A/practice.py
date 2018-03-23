"""
Test 
"""
__coinValues = {"pound":240, "shilling":12, "penny":1} 

class BritCoins:
    def __init__(self,**kwargs):
        self.totalPennies = 0
        for key in **kwargs:
            self.totalPennies= kwargs[key]*BritCoins.__coinValues[key]
    def __add__(self, other):
        total= self.totalPennies+other.totalPennies
        return total
            
        