class Player(object):
    def __init__(self, player_id, name, coin, protocol, image):
        self.player_id = player_id
        self.name = name
        self.coin = coin
        self.stack = 0
        self.protocol = protocol
        # 玩家状态，可能的状态为：
        # enter, sit, bring_scoreboard, ready: 进入房间,坐下, 带入筹码, 授权中, 准备开始
        self.status = 'enter'
        self.image = image
        self.geo_location = (0, 0)

    def bet_chips(self, bet_chips):
        self.stack -= bet_chips

    def bring_stack(self, stack):
        self.stack = stack

    def change_status(self, status):
        self.status = status

    def change_geo_location(self, geo_location):
        self.geo_location = geo_location