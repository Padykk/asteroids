from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return #jde o nejmenší asteroid, nesplituje se

        log_event("asteroid_split")
        rnd = random.uniform(20,50)
        first_velo = self.velocity.rotate(rnd)
        second_velo = self.velocity.rotate(-rnd)
        new_radiuses = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radiuses)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radiuses)
        new_asteroid1.velocity = first_velo * 1.2 #trošku je zrychlíme
        new_asteroid2.velocity = second_velo * 1.2
