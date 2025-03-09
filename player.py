from circleshape import CircleShape
from constants import *
import pygame

# Inherits from the CircleShape class in circleshape.py
class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen,color=(255,255,255),points=self.triangle(), width=2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt # Adds rotation to users current rotation

    def move(self,dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED *dt

    def update(self,dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # What happens when lowercase "a" is pressed (left)
            self.rotate(-dt)
        if keys[pygame.K_d]: # What happens when lowercase "d" is pressed (right)
            self.rotate(dt)
        if keys[pygame.K_w]: # What happens when lowercase "w" is pressed (move up)
            self.move(dt)
        if keys[pygame.K_s]: # What happens when lowercase "s" is pressed (move down)
            self.move(-dt)
