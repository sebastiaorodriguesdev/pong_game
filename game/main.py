import pygame
import sys
from rendering.render import draw_objects, set_game_window, render_game_score, render_pause_overlay
from setup.game_objects import instantiate_game_objects
from config.constants_config import WIDTH, HEIGHT
from logic.game_runner import run_game
pygame.init()
#game window
screen = set_game_window(WIDTH, HEIGHT)
#clock is to set fps
clock = pygame.time.Clock()
pygame.display.set_caption("Pong game")

running = True
paddles, input_handlers, ball, objectsToDraw, players, game_state = instantiate_game_objects() #setup paddles, balls, input handlers, game state

while running: 
    clock.tick(60) #60fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: #for single clicks and get_pressed for continuous
            if event.key == pygame.K_ESCAPE:
                if(game_state.state == "playing"):
                    game_state.state = "paused"
                elif(game_state.state == "paused"):
                    game_state.state = "playing"
        
    

    if game_state.state == "playing":
        for input_handler in input_handlers:
            input_handler.handle_input() #inside otherwise it will still move the paddles when not in game
        run_game(paddles, ball, players, WIDTH)
        draw_objects(objectsToDraw, screen)
        render_game_score(screen, pygame.font.SysFont("Arial", 20), players)
        pygame.display.update()
    elif game_state.state == "paused":
        render_pause_overlay(screen)
        pygame.display.update()
    
    
pygame.quit()
sys.exit()