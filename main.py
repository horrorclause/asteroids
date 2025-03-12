import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField


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

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Player object
    asteroidfield = AsteroidField()
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt) # Updates players location on the screen
        
        screen.fill((0,0,0)) # Fill the screen with a black background
        
        for object in drawable: # Drawing player on screen, has to be before display.flip()
            object.draw(screen)

        pygame.display.flip() # Update the full display Surface to the screen


        dt = clock.tick(60)/1000 # Setting to 60 FPS


        #-- Shows rotation and position for debugging --
        # print(f"Rotation: {player.rotation} Position: {player.position}", end="\r")

        


if __name__ == "__main__":
    main()