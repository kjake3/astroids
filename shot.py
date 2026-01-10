from constants import LINE_WIDTH, SHOT_RADIUS
# import pygame
import pygame
# import CircleShape class
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # draw a shot
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)