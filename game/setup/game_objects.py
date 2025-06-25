#game objects are instantiated here
from objects.paddle import Paddle
from objects.ball import Ball
from objects.input_handler import InputHandler
from objects.player import Player
import pygame
def instantiate_game_objects():
    paddle1 = Paddle(50, 250, 20, 100, (255, 255, 255))
    paddle2 = Paddle(725, 250, 20, 100, (255, 255, 255))
    paddles = [paddle1, paddle2]
    ball = Ball(400, 300, 10, (255, 255, 255)) 

    #players
    player1 = Player(1, "Player 1")
    player2 = Player(2, "Player 2")
    players = [player1, player2]
    #input handlers
    input_handler_paddle1 = InputHandler(paddle1, pygame.K_w, pygame.K_s)
    input_handler_paddle2 = InputHandler(paddle2, pygame.K_UP, pygame.K_DOWN)
    input_handlers = [input_handler_paddle1, input_handler_paddle2]

    drawables = paddles + [ball] #these are the objects which are going to be drawn
    return paddles, input_handlers, ball, drawables, players