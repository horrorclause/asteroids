import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity=pygame.Vector2(0,0)
        
    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius, 2)

    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)

        if  SCREEN_WIDTH > 0:
            self.position.x %= SCREEN_WIDTH
        if SCREEN_HEIGHT > 0:
            self.position.y %= SCREEN_HEIGHT
