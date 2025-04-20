import pygame
from constants import *
from player import *

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    fps = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        screen.fill("Black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()