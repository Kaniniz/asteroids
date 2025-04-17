import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        fps = pygame.time.Clock()
        dt = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("Black")
        player.draw(screen)
        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()