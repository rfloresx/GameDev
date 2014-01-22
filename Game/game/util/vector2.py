'''
Created on Jan 22, 2014

@author: otrebor
'''
import math

class Vector2:
    def __init(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def add(self,v2):
        return Vector2(self.x + v2.x, self.y + v2.y)
    
    def sub(self,v2):
        return Vector2(self.x - v2.x, self.y + v2.y)
    
    def scale(self,s):
        return Vector2(self.x*s, self.y*s)
    
    def magnitude(self):
        return math.sqrt(self.x*self.x+self.y+self.y)
    
    def normalize(self):
        m = self.magnitude()
        return Vector2(self.x/m,self.y/m)
    
    def distance(self, v2):
        return math.sqrt(  math.pow((self.x-v2.x),2) + math.pow((self.y-v2.y),2) )
    
    #distance square used on circle collision
    def distanceSq(self,v2):
        return math.pow((self.x-v2.x),2) + math.pow((self.y-v2.y),2)
    