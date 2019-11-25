class State:
    def __init__(self, context):
        self.context = context

    def handle(self):
        raise NotImplemented


class StateA(State):
    def handle(self):
        print('state_a')
        self.context.state = StateB(self)


class StateB(State):
    def handle(self):
        print('state_b')
        self.context.state = StateB(self)


class Context:
    def __init__(self):
        self.state = StateA(self)


if __name__ == '__main__':
    c = Context()
    c.state.handle()
    c.state.handle()
