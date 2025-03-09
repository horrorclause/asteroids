import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from player import Player
from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init() # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Assign the dimensions set in constants.py
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0)) # Fill the screen with a black background
        player.update(dt) # Updates players location on the screen
        player.draw(screen) # Drawing player on screen, has to be before display.flip()
        pygame.display.flip() # Update the full display Surface to the screen


        dt = clock.tick(60)/1000 # Setting to 60 FPS

        


if __name__ == "__main__":
    main()