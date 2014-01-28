'''
Created on Jan 15, 2014

@author: Otrebor45
'''
import sys
import time
import util.Vector2 as Vector2
import pygame
import scripts.ConstForse as ConstForse
import scripts.ApplySpeed as ApplySpeed
from pygame.locals import *

import world


class Game:
    GAMENAME = "null"
    
    INIT = False        
    def __init__ (self):
        self.INIT = True
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption(self.GAMENAME)
        
        self.world = world.World()
        circle = self.world.createRect(250,20,50,50,(255,0,255))
        circle.addComponent(ConstForse.ConstForse(circle,Vector2.Vector2(0,100) ))
        circle.addComponent(ApplySpeed.ApplySpeed(circle) )
        
        wall = self.world.createWall(0, 400, 500, 100, (0,0,0))
        
        
        
    def draw(self, delta):
        self.screen.fill((255, 255, 0))
        self.world.draw(self.screen)
        #pygame.draw.circle(self.screen,(0,0,0), (250,250),100, 0)
        pygame.display.flip()
        return
    
    def update(self, delta):
        pygame.event.pump()
        for evt in pygame.event.get():
            if evt.type == QUIT:
                pygame.quit()
                sys.exit()
        self.world.update(delta)
        
        return
    
    def run(self):
        if not self.INIT:
            self.init()
        oldtime = pygame.time.get_ticks()
        time.sleep(1)
        while True:
            newtime = pygame.time.get_ticks()
            delta = newtime - oldtime
            oldtime = newtime
            deltaf = delta/1000.0
            self.update(deltaf)
            self.draw(deltaf)
            
if __name__ == '__main__':
    g = Game()
    g.run()
    
        
