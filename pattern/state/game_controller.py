class InitLoop:
    def __init__(self, controller):
        self.controller = controller

    def bet(self):
        print('init bet')
        self.controller.state = ''


class SecondLoop:
    def __init__(self, controller):
        self.controller = controller


class GameController:
    def __init__(self):
        self.state = None
        self.init()

    def init(self):
        self.state = InitLoop(self)

    def bet(self):
        self.state.bet()


if __name__ == '__main__':
    controller = GameController()
    controller.bet()
