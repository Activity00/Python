class Cpu:
    def start(self):
        print('cpu start')


class Memory:
    def init(self):
        print('memeory init')


class Disk:
    def start(self):
        print('start')


class Computer:
    def __init__(self):
        self.cpu = Cpu()
        self.memory = Memory()
        self.disk = Disk()

    def start(self):
        self.cpu.start()
        self.memory.init()
        self.disk.start()


if __name__ == '__main__':
    computer = Computer()
    computer.start()
