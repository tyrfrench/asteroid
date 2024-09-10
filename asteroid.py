
import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)        

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255, 1), self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        direction1 = self.velocity.rotate(angle)
        direction2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = direction1 * 1.2
        new_asteroid2.velocity = direction2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt
