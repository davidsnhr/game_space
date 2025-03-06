import pygame

class Enemey:
    def __init__(self, x, y, sprite_path, speed=2):
        self.x = x
        self.y = y
        self.sprite_path = pygame.image.load(sprite_path)
        self.speed = speed

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.sprite_path, (self.x, self.y))
    