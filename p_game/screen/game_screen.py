import pygame

from p_game.manager.game_manager import GameManager
from p_game.screen import Screen


class GameScreen(Screen):
    color = (0, 0, 0)

    def __init__(self, manager):
        super().__init__(manager)
        self.game = GameManager()
        self.ball = pygame.image.load('ball.png')
        self.ball_rect = self.ball.get_rect()

    def update(self):
        self.manager.display.fill(self.color)
        self.manager.display.blit(self.ball, self.ball_rect)
        self.game.update()
