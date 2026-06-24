import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.position = (x, y)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        rotate_left = self.velocity.rotate(-angle)
        rotate_right = self.velocity.rotate(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_left = Asteroid(self.position.x, self.position.y, new_radius)
        new_right = Asteroid(self.position.x, self.position.y, new_radius)
        new_left.velocity = rotate_left * 1.2
        new_right.velocity = rotate_right * 1.2



