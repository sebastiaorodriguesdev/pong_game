import pygame
import sys
from rendering.render import draw_objects, set_game_window, render_game_score
from setup.game_objects import instantiate_game_objects
from config.constants_config import WIDTH, HEIGHT
from logic.collider_detection import check_collision
from logic.score_point import verify_point_score
from logic.score import player_score
pygame.init()

#game window
screen = set_game_window(WIDTH, HEIGHT)
#clock is to set fps
clock = pygame.time.Clock()
pygame.display.set_caption("Pong game")

running = True
paddles, input_handlers, ball, objectsToDraw, players = instantiate_game_objects() #setup paddles, balls, input handlers

while running: 
    clock.tick(60) #60fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    for input_handler in input_handlers:
        input_handler.handle_input()

    ball.update_position()
    check_collision(paddles, ball)
    
    scored, scoring_player = verify_point_score(ball, paddles[0], paddles[1])
    if scored:
        for player in players:
            if player.id == scoring_player:            
                player_score(player)
                ball.reset()
                print(player.name, player.score)
        
    draw_objects(objectsToDraw, screen)
    render_game_score(screen, pygame.font.SysFont("Arial", 20), players)
    pygame.display.update()

pygame.quit()
sys.exit()