# import constants
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
# import pygame
import pygame
# import CircleShape class
from circleshape import CircleShape
import random

from logger import log_event

# Astroid class
class Asteroid(CircleShape):
    
    # Astroid constructor
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    # draw an asteroid
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    # update the position of an asteroid
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        random_angle = random.uniform(20,  50)

        first_new_asteroid_vector = self.velocity.rotate(random_angle)
        second_new_asteroid_vector = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = first_new_asteroid_vector * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = second_new_asteroid_vector * 1.2



