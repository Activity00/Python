import sys

import pygame

from p_game.screen import ScreenManager
from p_game.screen.login_screen import LoginScreen

if __name__ == '__main__':
    pygame.init()
    size = width, height = 640, 480
    display = pygame.display.set_mode(size)
    screen_manager = ScreenManager(display, LoginScreen)
    clock = pygame.time.Clock()  # 设置时钟
    while True:
        clock.tick(60)  # 每秒执行60次
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        display.fill((0, 0, 0))
        screen_manager.update_screen()
        pygame.display.flip()

    pygame.quit()
