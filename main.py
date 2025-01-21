# Import all the good stuff
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    # Setup variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        # Handle ability to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Display background
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # Limit frame rate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()