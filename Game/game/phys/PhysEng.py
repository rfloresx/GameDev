'''
Created on Jan 22, 2014

@author: otrebor
'''
'''
Constant for collision types,
'''

import physutil
import game.phys.CircleCollider
import game.phys.RectCollider
import game.util.Vector2 as Vector2

class CollType:
    Circle = 1
    Rect = 2
        
class PhysEng:
    
    def __init__(self):
        self.objects = []
    
    
    def objCount(self):
        return len( self.objects)
    
    
    def add(self, obj):
        self.objects.append(obj)
        
    def remove(self, obj):
        self.objects.remove(obj)
    
    '''
    for each object in the list compared it to check if have collided with the other one
    if so, handle collision
    '''
    def update(self, delta):
        size = self.objCount()
        for i in range(0, size):
            for j in range(i, size):
                if i != j and not (self.objects[i].static and self.objects[j].static):  # is not the same and are not both static
                    self.handleCollision(self.objects[i], self.objects[j])
                
    '''
    identify collision case
    '''
    def handleCollision(self, obj1, obj2):
        case = self.getCollisionType(obj1, obj2)
        
        if case[0] == 0 or case[1] == 0:  # error
            return -1
        elif self.cmp(case, (CollType.Circle, CollType.Circle)):  # gamecode gamecode
            if self.checkCircleCircleCollision(obj1, obj2):
                self.fixPosCircleCircle(obj1, obj2)
                physutil.collideCircleCirlce(obj1, obj2)
                
        elif self.cmp(case, (CollType.Circle, CollType.Rect)):  # gamecode rectangle
            if self.checkCircleRectCollision(obj1, obj2):
                self.fixPosCircleRect(obj1, obj2)
                physutil.collideCircleRect(obj1, obj2)
     
        elif self.cmp(case, (CollType.Rect, CollType.Circle)):  # rectangle gamecode
            if self.checkCircleRectCollision(obj2, obj1):
                self.fixPosCircleRect(obj2, obj1)
                physutil.collideCircleRect(obj2, obj1)
  
        elif self.cmp(case, (CollType.Rect, CollType.Rect)):  # rectangle rectangle
            if self.checkRectRectCollision(obj1, obj2):
                self.fixPosRectRect(obj1, obj2)
                physutil.collideRectRect(obj1, obj2)
    
    def cmp(self, t1 = (0,0), t2 = (0,0)):
        return t1[0] == t2[0] and t1[1] == t2[1]
    '''
    ================Collision handling push back=========
    '''
    
    
    
    '''
    ================Collision repositioning==============
    '''
    
    '''
    function to identify Collision types, 
    return (obj1CollTypeId, obj2CollTYpeId)
    '''
    def getCollisionType(self, obj1, obj2):
        x, y = 0, 0
        
        if isinstance(obj1, game.phys.CircleCollider.CircleCollider):  # first object is gamecode
            x = CollType.Circle     
        elif isinstance(obj1, game.phys.RectCollider.RectCollider):  # first object is rectangle
            x = CollType.Rect
        
        if isinstance(obj2, game.phys.CircleCollider.CircleCollider):  # second object is gamecode
            y = CollType.Circle           
        elif isinstance(obj2, game.phys.RectCollider.RectCollider):  # second object is rectangle
            y = CollType.Rect
            
        return (x, y)
    
    def fixPosCircleCircle(self, c1, c2):
        pos1 = c1.pos()
        pos2 = c2.pos()
        dif = pos2.sub(pos1)
        
        if c1.static:
            c2.setPos(pos2.add(dif))
        elif c2.static:
            c1.setPos(pos1.add(dif.scale(-1)))
        else:
            c1.setPos(pos1.add(dif.scale(-.5)))
            c2.setPos(pos2.add(dif.scale(.5)))
        
    def fixPosCircleRect(self, c1, r2):
        colPos = physutil.getCollisionPosition2(physutil.circleToRect(c1) , r2)
        if(colPos[0] == 0 or colPos[1] == 0):
            pos = Vector2.Vector2(colPos[0], colPos[1])
            pos1 = c1.pos()
            pos2 = r2.pos()
            if c1.static:
                r2.setPos(pos2.add(pos))
            elif r2.static:
                c1.setPos(pos1.add(pos.scale(-1)))
            else:
                c1.setPos(pos1.add(pos.scale(-.5)))
                r2.setPos(pos2.add(pos.scale(.5)))
        else:
            pos1 = c1.pos()
            pos2 = r2.pos()
            dif = pos2.sub(pos1)
        
            if c1.static:
                r2.setPos(pos2.add(dif))
            elif r2.static:
                c1.setPos(pos1.add(dif.scale(-1)))
            else:
                c1.setPos(pos1.add(dif.scale(-.5)))
                r2.setPos(pos2.add(dif.scale(.5)))
           
    def fixPosRectRect(self, r1, r2):
        colPos = physutil.getCollisionPosition(r1, r2)
        pos = Vector2.Vector2(colPos[0], colPos[1])
        pos1 = r1.pos()
        pos2 = r2.pos()
        if r1.static:
            r2.setPos(pos2.add(pos))
        elif r2.static:
            r1.setPos(pos1.add(pos.scale(-1)))
        else:
            r1.setPos(pos1.add(pos.scale(-.5)))
            r2.setPos(pos2.add(pos.scale(.5)))
    
    
    ''' ===============Check Collisions================'''
    
    '''
    gamecode vs gamecode collision detection
    '''
    def checkCircleCircleCollision(self, c1, c2):
        r = c1.radius + c2.radius
        r = r * r
        rsq = c1.pos().distanceSq(c2.pos())
        return r < rsq
    
    '''
    rectangle vs rectangle collision detection
    '''
    def checkRectRectCollision(self, r1, r2):
        return not (r1.bottom() < r2.top() or 
                     r1.top() > r2.bottom() or 
                     r1.left() > r2.right() or
                     r1.right() < r2.left())
        
    '''
    gamecode vs rectangle collision detection
    '''
    def checkCircleRectCollision(self, c, re):
        return self.checkCircleCircleCollision(c, physutil.rectToCircle(re)) and self.checkRectRectCollision(physutil.circleToRect(c), re)
    
    
    
    
    
