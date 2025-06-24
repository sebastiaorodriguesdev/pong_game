from objects.paddle import Paddle
from objects.ball import Ball
from logic.input_handler import InputHandler
import pygame
def instantiate_game_objects():
    paddle1 = Paddle(50, 250, 20, 100, (255, 255, 255))
    paddle2 = Paddle(725, 250, 20, 100, (255, 255, 255))
    paddles = [paddle1, paddle2]

    ball = Ball(400, 300, 20, 20, (255, 255, 255))

    input_handler_paddle1 = InputHandler(paddle1, pygame.K_w, pygame.K_s)
    input_handler_paddle2 = InputHandler(paddle2, pygame.K_UP, pygame.K_DOWN)
    input_handlers = [input_handler_paddle1, input_handler_paddle2]

    return paddles, input_handlers, ball