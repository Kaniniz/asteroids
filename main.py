import pygame
import sys
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    fps = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for ast in asteroids:
            for bullet in shots:
                if ast.collision_check(bullet):
                    ast.split()
                    bullet.kill()

            if ast.collision_check(player):
                print("Game over!")
                sys.exit()
            
        
        screen.fill("Black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()