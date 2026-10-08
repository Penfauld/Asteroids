from constants import (PLAYER_RADIUS, LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED)
from circleshape import CircleShape
from shot import Shot
import pygame


class Player(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    def rotate(self, dt) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt
    def move(self, dt) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.timer > 0:
            return
        else:
            self.timer = PLAYER_SHOOT_COOLDOWN_SECONDS

        shot = Shot(self.position.x, self.position.y)
        shot_vector = pygame.Vector2(0,1)
        rotated = shot_vector.rotate(self.rotation)
        shot.velocity = rotated * PLAYER_SHOOT_SPEED

    def update(self, dt: float) -> None:
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
                self.rotate(-dt)
        if keys[pygame.K_d]:
                self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
