import pygame
import sys
from rendering.render import draw_objects, set_game_window
from setup.game_objects import instantiate_game_objects
from config.constants_config import WIDTH, HEIGHT
pygame.init()

#game window
screen = set_game_window(WIDTH, HEIGHT)
#clock is to set fps
clock = pygame.time.Clock()
pygame.display.set_caption("Pong game")

running = True
paddles, input_handlers, ball = instantiate_game_objects() #setup paddles, balls, input handlers
objectsToDraw = paddles + [ball]

while running: 
    clock.tick(60) #60fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    for input_handler in input_handlers:
        input_handler.handle_input()

    draw_objects(objectsToDraw, screen)
    pygame.display.update()

pygame.quit()
sys.exit()