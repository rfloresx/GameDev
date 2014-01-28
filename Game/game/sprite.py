'''
Created on Jan 22, 2014

@author: otrebor
'''
import pygame


class Sprite:
    
    # sprite constructor
    def __init__(self, img, x, y, w, h):
        self.img = img
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        pass
    
    # draw sprite
    def draw(self, screen):
        if self.pos != None:
            pos = self.pos()
            self.x = pos.x - self.w / 2
            self.y = pos.y - self.h / 2
            
        if self.img != None:
            screen.blit(self.img, pygame.rect.Rect(self.x, self.y, self.w, self.h))
    

        
