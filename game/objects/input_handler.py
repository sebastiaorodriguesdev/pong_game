import pygame
from logic.paddle_movement import movePaddle
class InputHandler:
    def __init__(self, paddle, up_key, down_key, game_state):
        self.paddle = paddle
        self.up_key = up_key
        self.down_key = down_key
        self.game_state = game_state
        
    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[self.up_key]:
            movePaddle(self.paddle, "up")
        elif keys[self.down_key]:
            movePaddle(self.paddle, "down")
        