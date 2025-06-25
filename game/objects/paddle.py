import pygame


class Paddle:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 255, 255)
        

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def move(self, direction):
        speed = 10
        if direction == "up" and self.rect.y > 0:
            self.rect.y -= speed
        elif direction == "down" and self.rect.y + self.rect.height < 600: #because the rect is 100px high, so we need to count with the height
            self.rect.y += speed