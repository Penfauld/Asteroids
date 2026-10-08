from circleshape import CircleShape
from constants import (LINE_WIDTH, ASTEROID_MIN_RADIUS)
from logger import log_event
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            log_event("asteroid_kill")
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            vel1 = self.velocity.rotate(angle)
            vel2 = self.velocity.rotate(-angle)
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid1.velocity = vel1 * 1.2
            asteroid2.velocity = vel2 * 1.2
