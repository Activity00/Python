class SensitiveInfo:
    def __init__(self):
        self.users = ['nick', 'tom']

    def read(self):
        print(f'user info: {self.users}')

    def add(self, user):
        self.users.append(user)
        print('add a user')


class Info:
    def __init__(self):
        self.protected = SensitiveInfo()
        self.screct = 'xxxx'

    def read(self):
        self.protected.read()

    def add(self, user):
        self.protected.add(user)
