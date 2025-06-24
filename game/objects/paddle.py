import pygame


class Paddle:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 255, 255)
        

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def move(self, direction):
        if direction == "up":
            self.rect.y -= 5
        elif direction == "down":
            self.rect.y += 5