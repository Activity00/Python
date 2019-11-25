import pygame


class Screen:
    def __init__(self, manager):
        self.manager = manager

    def update(self):
        pass


class LoginScreen(Screen):
    color = (0, 0, 0)

    def __init__(self, manager):
        super().__init__(manager)
        self.ball = pygame.image.load('ball.png')
        self.ball_rect = self.ball.get_rect()
        self.speed = [5, 5]  # 设置移动的X轴、Y轴

    def update(self):

        self.ball_rect = self.ball_rect.move(self.speed)  # 移动小球
        # 碰到左右边缘
        if self.ball_rect.left < 0 or self.ball_rect.right > 640:
            self.speed[0] = -self.speed[0]
            self.manager.replace_screen(MainScreen)
        # 碰到上下边缘
        if self.ball_rect.top < 0 or self.ball_rect.bottom > 480:
            self.speed[1] = -self.speed[1]

        self.manager.display.fill(self.color)
        self.manager.display.blit(self.ball, self.ball_rect)


class MainScreen(Screen):
    pass


class ScreenManager:
    def __init__(self, display, screen_cls):
        self.screen = screen_cls(self)
        self.display = display

    def update_screen(self):
        self.screen.update()

    def replace_screen(self, screen_cls):
        self.screen = screen_cls(self)
