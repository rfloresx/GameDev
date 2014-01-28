'''
Created on Jan 22, 2014

@author: otrebor
'''

import Collider
import game.util.Vector2 as Vector2

class CircleCollider(Collider.Collider):
    def __init__(self, gameObject=None, x=0,y=0, radius=0):
        Collider.Collider.__init__( self,gameObject)
        self.radius = radius
        self.position = Vector2.Vector2(x,y)
