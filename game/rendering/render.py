import pygame
def draw_objects(objects, screen):
    screen.fill((0, 0, 0))
    for obj in objects:
        obj.draw(screen)

def set_game_window(WIDTH, HEIGHT):
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    return screen