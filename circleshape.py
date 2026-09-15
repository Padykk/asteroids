import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    # Sprite je jednoduchá class pro viditelné game objekty
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

    def collides_with(self, other):
        max_distance = self.radius + other.radius
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        if distance <= max_distance:
            return True
        return False
