from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position , self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        angle1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        angle2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new1 = Asteroid(self.position[0], self.position[1], new_radius)
        new2 = Asteroid(self.position[0], self.position[1], new_radius)
        new1.velocity = angle1 * 1.2
        new2.velocity = angle2 * 1.2