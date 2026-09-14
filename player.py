from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH
import pygame

class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # vytvoří trojúhelník (pro model hráče -> draw)
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        #override z CircleShape

        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        # vykreslí model Player
        # screen = kam?
        # color = v jaké barvě?
        # points = tuple nebo list souřadnic
        # width = šířka čar pro vykreslení
