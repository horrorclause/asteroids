from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)


    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius, 2)
    
    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)

        if SCREEN_WIDTH > 0:
            self.position.x %= SCREEN_WIDTH
        if SCREEN_HEIGHT > 0:
            self.position.y %= SCREEN_HEIGHT

    def split(self):

        self.kill()
        
        random_angle = random.uniform(20,50)
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle1 = self.velocity.rotate(random_angle)
        angle2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        new_asteroid1.velocity = angle1 * 1.2
        new_asteroid2.velocity = angle2 * 1.2