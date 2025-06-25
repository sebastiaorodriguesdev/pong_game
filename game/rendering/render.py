import pygame
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
        
            
        