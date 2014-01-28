'''
Created on Jan 28, 2014

@author: otrebor
'''
import GameObject
import game.phys.CircleCollider as CircleCollider 
import Object

import pygame

class CircleObject(GameObject.GameObject):
    def __init__(self,x, y, r, collor):
        GameObject.GameObject.__init__(self)
        
        self.collor = collor
        self.collider = CircleCollider.CircleCollider(self,x,y, r)
        self.render = Object.Object()
        self.render.draw = lambda screen: self.drawCircle(screen)
        self.pos = lambda: self.collider.pos()
        
        
    def drawCircle(self, screen):
        pos = self.collider.pos()
        pygame.draw.circle(screen, self.collor, (int(pos.x), int(pos.y)), int(self.collider.radius))
        
        
        
        
        
        