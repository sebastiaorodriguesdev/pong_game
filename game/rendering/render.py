import pygame
from config.constants_config import WIDTH, HEIGHT
def draw_objects(objects, screen):
    screen.fill((0, 0, 0))
    for obj in objects:
        obj.draw(screen)

def set_game_window(WIDTH, HEIGHT):
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    return screen

def render_game_score(screen, font, players):
    initial_x, counter = 10,  0

    for player in players:
        if counter > 0:
            player.draw(screen, initial_x + 700, 10, font, (255, 255, 255))
        else:
            player.draw(screen, initial_x, 10, font, (255, 255, 255))
            counter += 1
        
def render_pause_overlay(screen):
    font = pygame.font.SysFont("Arial", 40)
    text = font.render("PAUSED", True, (255, 255, 255))
    screen.blit(text, (
        WIDTH // 2 - text.get_width() // 2,
        HEIGHT // 2 - text.get_height() // 2
    ))
            
        