'''
Created on Jan 22, 2014

@author: otrebor
'''
from game.util.vector2 import Vector2
import phyObj

class CircleCollider(phyObj):
    def __init__(self,radius = 0, position=Vector2(0,0)):
        self.radius = radius
        self.pos = position
        
    

    def checkCircleCollision(self,other):
        r = self.radius + other.radius
        r = r * r
        rsq = self.pos.distanceSq(other.pos)
        return r < rsq
    
    
    