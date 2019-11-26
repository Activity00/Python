class Screen:
    def __init__(self, manager):
        self.manager = manager

    def update(self):
        pass


class ScreenManager:
    def __init__(self, display, screen_cls):
        self.screen = screen_cls(self)
        self.display = display

    def update_screen(self):
        self.screen.update()

    def replace_screen(self, screen_cls):
        self.screen = screen_cls(self)
