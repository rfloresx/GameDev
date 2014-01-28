'''
Created on Jan 22, 2014

@author: otrebor
'''
'''
physical object template
'''

import game.base.Component as Component
import game.util.Vector2 as vector2


class Collider( Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__( self,gameObject)
        # my change to separate component
        self.position = vector2.Vector2()
        self.speed = vector2.Vector2()  # initialize velocity to zero
        self.static = False
    
    
    # just a hack
    def mass(self):
        if self.static:
            return 1000000000
        return 1
    
    def pos(self):
        return self.position
    
    def setPos(self, pos):
        self.position = pos
    

    # must move to other script
    
    def setSpeed(self, speed):
        self.speed = speed
    
    def update(self, delta):
        if not self.static:
            self.position = self.position.add(self.speed.scale(delta))
        pass
