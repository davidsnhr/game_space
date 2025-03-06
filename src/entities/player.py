import pygamge
from entities.bullet import Bullet

class Player:
    def __init__(self, x, y,sprite_path):
        self.x = x
        self.y = y
        self.speed = 5
        self.sprite_path = pygamge.load_image(sprite_path)
    
    def shoot(self):
        return Bullet(self.x+20, self.y )
    
    def move(self, keys, width):
        if keys[pygamge.K_LEFT] and self.x < 0:
            self.x -= self.speed
        if keys[pygamge.K_RIGHT] and self.x  < width - 50:
            self.x += self.speed
    
    def draw(self, screen):
        screen.draw_image(self.sprite_path, (self.x, self.y))
    