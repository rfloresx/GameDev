'''
Created on Jan 28, 2014

@author: otrebor
'''
import GameObject
import Object
import game.phys.RectCollider as RectCollider
import pygame

class RectObject(GameObject.GameObject):
    def __init__(self, x, y, w, h, color):
        GameObject.GameObject.__init__(self)
        self.color = color
        self.collider = RectCollider.RectCollider(self,x+w/2, y+h/2, w, h)
        self.render = Object.Object()
        self.render.draw = lambda screen: self.drawRect(screen)
        self.pos = lambda: self.collider.pos()
        
        
    def rect(self):
        return pygame.rect.Rect(self.collider.left(), self.collider.top(), self.collider.w, self.collider.h)
        
    def drawRect(self, screen):
        pygame.draw.rect(screen, self.color, self.rect())
        