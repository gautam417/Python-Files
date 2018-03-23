"""
Gautam Mehta
ICE_J
"""
import math
class Parent:#Circle Class
    def __init__ (self, radius):
        self.radius= radius
    def getArea (self):
        self.area= (math.pi)*self.radius*self.radius
        return self.area
       
        
class Child(Parent):#Cylinder Class
    def __init__ (self,radius,height):
        radius= Parent.__init__(self, radius)
        self.height=height
    def getVolume (self):
        self.vol = (Parent.getArea(self))*self.height
        return self.vol
c=Parent(4)
c.getArea()
print ("Circle area is:", round(c.area,2))

cy=Child(2,5)
cy.getVolume()
print ("Cylinder volume is:", round(cy.vol,2))