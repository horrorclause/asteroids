import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init() # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Assign the dimensions set in constants.py
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Player object
    asteroidfield = AsteroidField()
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt) # Updates players location on the screen

        for object in asteroids:
            if object.colliding_with(player):
                print("Game Over!")
                sys.exit()
        
        for asteroid in asteroids: # Checks for bullet/asteroid collisions
            for bullet in shots:
                if asteroid.colliding_with(bullet):
                    bullet.kill()
                    asteroid.split() # Checks if an asteroid is large enough to be split

        screen.fill((0,0,0)) # Fill the screen with a black background
        
        for object in drawable: # Drawing player on screen, has to be before display.flip()
            object.draw(screen)

        pygame.display.flip() # Update the full display Surface to the screen


        dt = clock.tick(60)/1000 # Setting to 60 FPS


        #-- Shows rotation and position for debugging --
        # print(f"Rotation: {player.rotation} Position: {player.position}", end="\r")

        


if __name__ == "__main__":
    main()