import pygame
import random
class Ball():
    def __init__(self, x, y, radius, color):
        super().__init__()
        self.x = x
        self.y = y
        self.intial_x = x
        self.intial_y = y
        self.radius = radius
        self.color = color
        
        self.velocity_x = random.choice([-1, 1]) * random.randint(4, 6) #speed variation
        self.velocity_y = random.choice([-1, 1]) * random.randint(4, 6)
        self.hitbox = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.radius)
    
    def update_position(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.hitbox.x = self.x - self.radius
        self.hitbox.y = self.y - self.radius
        if self.hitbox.x < 0 or self.hitbox.x + self.radius > 800:
            self.velocity_x *= -1
        if self.y < 0 or self.y > 600:
            self.velocity_y *= -1
    
    def reset(self):
        self.x = self.intial_x
        self.y = self.intial_y

        self.velocity_x = random.choice([-1, 1]) * random.randint(4, 6) #speed variation
        self.velocity_y = random.choice([-1, 1]) * random.randint(4, 6)

        #updating hitbox just to be sure it still is attached correctly to the box
        self.hitbox.x = self.x - self.radius
        self.hitbox.y = self.y - self.radius