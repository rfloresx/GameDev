'''
Created on Jan 27, 2014

@author: otrebor
'''

class GameObject:
    def __init__(self):
        self.collider = None
        self.render = None
        self.components = []
        
    def setPos(self, pos):
        if self.collider != None:
            self.collider.setPos(pos)
            
    def setVel(self, vel):
        if self.collider != None:
            self.collider.setVel(vel)
    
    def addVel(self, acc):
        if self.collider != None:
            self.collider.addVel(acc)
    
    '''
        Component is a lambda self,delta: {}
    '''
    def addComponent(self, component):
        if component != None:
            self.components.append(component)
    
    def update(self, delta):
        if self.components == None:
            return
        for c in self.components:
            if c != None and c.update != None:
                c.update(delta)
        
    def draw(self, screen):
        if self.render != None:
            self.render.draw(screen)
