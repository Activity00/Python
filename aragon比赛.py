# coding: utf-8

"""
@author: 武明辉 
@time: 18-8-8 下午7:01
"""
import math
import time

import requests

"""
域名是 shapan.test01.aragoncs.cn
比赛采取积分赛，两两互相对决，每个人当一次先手，一次后手。赢的3分，平的1分，输的0分
比赛有可能会出现平局，主要是场上部队同时被清理掉了，就是平局
最后按照积分多少，进行排名
虑到我们这个是编程大赛，不是即时战略游戏大赛，所以原来说的可以手动调整某个部队的规则，现在取消，程序只能根据取到的场上情况，去决定下一步怎么走，
不允许手动进行操作比赛整个流程没有大的变化，但是接口有调整，所以在这里说一下

1. 进入房间，例子：
http://shapan.test01.aragoncs.cn/join-room/?room_id=1&player_id=1&position=0&formation=0000000000q0000000000000000000q0q00000000000000000q0q0q000000000000000g0g0g0g0000000
post请求，？后面为post参数。room_id为房间号，player_id为玩家号，position为先后手，0为先手，在战场左边，1为后手，在战场右边，formation为阵型，84长度的字符串。第一组21个字符对应的最前排部队，第二组对应第二排，如此类推
阵型0，代表该位置不部署部队，为q，代表骑兵，为g，代表弓兵，为b，代表步兵。各兵种特性：q，移动时移动2步，如果移动1步后不能继续移动，则剩下1步进行攻击。g，攻击距离4，攻击距离为1的敌人时，伤害减半。b，攻击q时，伤害加倍

2. 改变军队位置，例如：
http://shapan.test01.aragoncs.cn/set-army-directions/?room_id=1&player_id=1&directions=6666666666
post请求，？后面为post参数。directions为10各部队的方向，每次请求同时改动10个部队的方向，每一次移动只能改动一次。10个部队先后顺序为从上到下，从前到后。则最前排最上面的第一个队伍为队伍1

3. 获取房间信息，例如：
http://shapan.test01.aragoncs.cn/get-room-info/?room_id=1

get请求
两个辅助测试请求，用浏览器访问：
http://shapan.test01.aragoncs.cn/watch-room/?room_id=1，观察战场情况，手动刷新
http://shapan.test01.aragoncs.cn/reset-room/?room_id=1，重置房间

这个为人员名单，每个人使用的房间号为对应的序号，例如霍小明使用房间1。每个人使用的用户号为对应的序号，以及100+序号。例如霍小明使用的用户号为1和101
每个人分配2个用户号的目的，是让你自己能进去两个玩家，这样房间才能开始。你可以集中写一个代码，另外一个玩家则使用浏览器发送一个固定的http请求进入房间，不做任何额外操作
如果有不懂游戏规则的，可以先发起两个post请求，进房间，然后用watch room请求，刷新战场状态，看看战场是怎么发展的
正式比赛时，会要求你们进入指定的房间，指定的位置。所以你们写的程序必须得能修改这两个参数。用户id的话，可以写死序号
方向一共是8个方向，上，右上，右，右下，下，左下，左，左上。对应0，1，2，3，4，5，6，7
晚上上来再啰嗦2句。有些同学没搞明白几个兵种的行动逻辑。大概伪代码写一下。
弓兵，步兵：

尝试攻击
如果没有攻击目标
        尝试移动


骑兵：

尝试攻击
如果没有攻击目标
        尝试移动一步
        尝试攻击
        如果没有攻击目标
                尝试移动一步

攻击逻辑：
步兵：
看看前方一格是否有敌人
有敌人，计算伤害，如果敌人是骑兵，伤害乘2

弓兵：
看看前方一格，两格，三格，四格是否有敌人，找最近的一个
有敌人，计算伤害，如果敌人跟自己的距离是1，伤害除2
骑兵：
看看前方一格是否有敌人
有敌人，计算伤害

基本上，第一个版本，做到能接收房间号，位置，阵型3个参数，调用成功，那么就能比赛了。第二个版本，就要做到定时获取房间信息，1秒1次够了，然后根据策略，设置各部队方向。这个策略，就看水平了

今天有人问了一个问题，说房间号，位置，阵型，怎么接收。我解释一下这3个参数吧。每一场比赛，我们都会找两个人来比，例如第一场是张雪对杨帆。那我就会说，张雪进1号房间0号位置，杨帆进1号房间1号位置。所以说房间号和位置是我分配的，你们的代码得有方法输入我这个房间号和位置的参数
至于阵型，同样是一个输入参数。我第一场直接上了10个骑兵，然后效果不好，然后我第二场要换一下，那得有地方能换。如果你不换，自然可以写死这个参数
比赛的时候，是自己运行自己的代码 还是提交到某处裁判来运行？
自己运行自己的，不过要求你们进场以后就离手
意思是如果是用电脑参加比赛的，就手离开键盘，如果是手机参加比赛的，就手离开手机
进场以后，开始比赛了，就不能再干预了，全部都只能是代码进行
允许把初始阵型配置成常量，进行修改么？
A和B比赛完，A和B都不会马上参加下一场，下一场可能是C和D
重复一下，每个人使用的用户id为两个，序号和序号+100，房间号为序号
不要随意设置
房间跑完了，使用reset room的地址来重置

"""
"""
1. 进入房间，例子：
http://shapan.test01.aragoncs.cn/join-room/?room_id=1&player_id=1&position=0&formation=0000000000q0000000000000000000q0q00000000000000000q0q0q000000000000000g0g0g0g0000000
post请求，？后面为post参数。room_id为房间号，player_id为玩家号，position为先后手，0为先手，在战场左边，1为后手，在战场右边，formation为阵型，84长度的字符串。第一组21个字符对应的最前排部队，第二组对应第二排，如此类推
阵型0，代表该位置不部署部队，为q，代表骑兵，为g，代表弓兵，为b，代表步兵。各兵种特性：q，移动时移动2步，如果移动1步后不能继续移动，则剩下1步进行攻击。g，攻击距离4，攻击距离为1的敌人时，伤害减半。b，攻击q时，伤害加倍

2. 改变军队位置，例如：
http://shapan.test01.aragoncs.cn/set-army-directions/?room_id=1&player_id=1&directions=6666666666
post请求，？后面为post参数。directions为10各部队的方向，每次请求同时改动10个部队的方向，每一次移动只能改动一次。10个部队先后顺序为从上到下，从前到后。则最前排最上面的第一个队伍为队伍1

3. 获取房间信息，例如：
http://shapan.test01.aragoncs.cn/get-room-info/?room_id=1
{"state": "playing", "battleground": 
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, {"army_type": "g", "hp": 1000, "order": 12, "direction": 2, "player_id": 1}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {"army_type": "g", "hp": 1000, "order": 13, "direction": 6, "player_id": 101}, 0], [0, 0, 0, {"army_type": "q", "hp": 1000, "order": 6, "direction": 2, "player_id": 1}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {"army_type": "q", "hp": 1000, "order": 7, "direction": 6, "player_id": 101}, 0, 0, 0], 
    [0, {"army_type": "g", "hp": 1000, "order": 14, "direction": 2, "player_id": 1}, 0, 0, {"army_type": "q", "hp": 1000, "order": 2, "direction": 2, "player_id": 1}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {"army_type": "q", "hp": 1000, "order": 3, "direction": 6, "player_id": 101}, 0, 0, {"army_type": "g", "hp": 1000, "order": 15, "direction": 6, "player_id": 101}, 0], [0, 0, 0, {"army_type": "q", "hp": 1000, "order": 8, "direction": 2, "player_id": 1}, 0, {"army_type": "q", "hp": 1000, "order": 0, "direction": 2, "player_id": 1}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {"army_type": "q", "hp": 1000, "order": 1, "direction": 6, "player_id": 101}, 0, {"army_type": "q", "hp": 1000, "order": 9, "direction": 6, "player_id": 101}, 0, 0, 0], [0, {"army_type": "g", "hp": 1000, "order": 16, "direction": 2, "player_id": 1}, 0, 0, {"army_type": "q", "hp": 1000, "order": 4, "direction": 2, "player_id": 1}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {"army_type": "q", "hp": 1000, "order": 5, "direction": 6, "player_id": 101}, 0, 0, {"army_type": "g", "hp": 1000, "order": 17, "direction": 6, "player_id": 101}, 0], [0, 0, 0, {"army_type": "q", "hp": 1000, "order": 10, "direction": 2, "player_id": 1}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {"army_type": "q", "hp": 1000, "order": 11, "direction": 6, "player_id": 101}, 0, 0, 0], [0, {"army_type": "g", "hp": 1000, "order": 18, "direction": 2, "player_id": 1}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {"army_type": "g", "hp": 1000, "order": 19, "direction": 6, "player_id": 101}, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "step": 1, "winner": -1, "server_time": 1533787004.0226169, "last_step_time": 1533787003.9126441}
    
游戏中，每一个移动周期，称为1步，在get room info中，通过step返回
step <= 50，每5步，左右压缩
step > 50，每5步，四周压缩
    
"""
PLAYER_ID = 6
ROOM_ID = 19
POSITION = 1
EMPTY_ID = 9
# #############$$$$$$$$$$$$$$$$$$$$$#####################$$$$$$$$$$$$$$$$$$$$$#####################
INFORMATION = '00000000g0g0g000000000000000000q0q0q00000000000000g000g000000000000000b0b00000000000'


def calc_angle(x_point_s, y_point_s, x_point_e, y_point_e):
    angle = 0
    y_se = y_point_e-y_point_s
    x_se = x_point_e-x_point_s
    if x_se == 0 and y_se > 0:
        angle = 360
    if x_se == 0 and y_se < 0:
        angle = 180
    if y_se == 0 and x_se > 0:
        angle = 90
    if y_se == 0 and x_se < 0:
        angle = 270
    if x_se > 0 and y_se > 0:
       angle = math.atan(x_se/y_se)*180/math.pi
    elif x_se < 0 and y_se > 0:
       angle = 360 + math.atan(x_se/y_se)*180/math.pi
    elif x_se<0 and y_se<0:
       angle = 180 + math.atan(x_se/y_se)*180/math.pi
    elif x_se>0 and y_se<0:
       angle = 180 + math.atan(x_se/y_se)*180/math.pi
    return angle


class Solider:
    def __init__(self, order, position, hp, direction, manager):
        self.order = order
        self.position = position
        self.hp = hp
        self.direction = direction
        self.manager = manager

    @property
    def attack(self):
        return int(self.hp * 0.1)

    def next_direction(self):
        enemy = self.manager.nearlest_enemy(self)
        return self.direction(enemy)

    def in_attack_range(self):
        pass

    def enemy_target(self, enemy):
        target = 2
        du = calc_angle(self.position[0], self.position[1], enemy.position[0], enemy.position[1])
        if du <= 23 or du >= 338:
            target = 4
        elif 22 <= du <= 68:
            target = 3
        elif 68 <= du <= 113:
            target = 2
        elif 113 <= du <= 157:
            target = 1
        elif 157 <= du <= 203:
            target = 7
        elif 203 <= du <= 225:
            target = 6
        elif 226 <= du <= 337:
            target = 5
        return target

    def direction(self, enemy):
        target = self.enemy_target(enemy)
        if self.is_wall(target):
            target = target - 4 if target + 4 > 7 else target + 4
        return target

    def is_wall(self, target):
        if target == 0:
            return self.manager.is_wall(self.position[0], self.position[1]-2)
        elif target == 1:
            return self.manager.is_wall(self.position[0]+2, self.position[1]-2)
        elif target == 2:
            return self.manager.is_wall(self.position[0] + 2, self.position[1])
        elif target == 3:
            return self.manager.is_wall(self.position[0] + 2, self.position[1]+2)
        elif target == 4:
            return self.manager.is_wall(self.position[0], self.position[1]+2)
        elif target == 5:
            return self.manager.is_wall(self.position[0]-2, self.position[1]+2)
        elif target == 6:
            return self.manager.is_wall(self.position[0]-2, self.position[1])
        elif target == 7:
            return self.manager.is_wall(self.position[0]-2, self.position[1]+2)


class GSolider(Solider):
    attack_range = 4


class QSolider(Solider):
    attack_range = 2


class BSolider(Solider):
    attack_range = 1


class Manager:

    def __init__(self, room_id, player_id, position):
        self.room_id = room_id
        self.player_id = player_id
        self.position = position
        self.heros = {}
        self.enemies = {}
        self.battleground = [[0]*41]*21
        self.last_upd_time = 0  # 上次更新时间

    def reset_room(self):
        try:
            requests.get('http://shapan.test01.aragoncs.cn/reset-room/?room_id={}'.format(self.room_id))
        except TimeoutError:
            print('重置房间超时')

    def enter_room(self, information):
        try:
            response = requests.post(
                'http://shapan.test01.aragoncs.cn/join-room/?room_id={}&player_id={}&position={}&formation={}'.format(
                    self.room_id, self.player_id, self.position, information
                )).json()
            if not response.get('success'):
                raise Exception('进入房间错误', response.get('success'))
            return True
        except Exception as e:
            print(e)
            return False

    def start(self):
        # 主循环
        while True:
            # 获取房间信息
            response = requests.get(
                'http://shapan.test01.aragoncs.cn/get-room-info/?room_id={}'.format(self.room_id)
            )
            try:
                response = response.json()
                if response.get('state') == 'waiting':
                    raise Exception
            except:
                print('等待对手进入房间...')
                time.sleep(1)
                continue

            if response.get('last_step_time') == self.last_upd_time:
                time.sleep(0.1)  # 获取房间信息频率
                continue
            self.last_upd_time = response.get('last_step_time')

            if response.get('state' == 'over'):
                msg = '赢了' if response.get('winner') == POSITION else '输了'
                print(msg)
                break

            self.battleground = response.get('battleground')
            self._update_soliders()     # 更新士兵对象
            self._directions()          # 设置最优方向

    def _directions(self):
        ds = {}
        for hero in self.heros:
            ds[hero.order] = str(hero.next_direction())
        directions = ''
        for i in range(10):
            directions += ds.get(i, 0)
        try:
            requests.post(
                'http://shapan.test01.aragoncs.cn/set-army-directions/?room_id={}&player_id={}&directions={}'.
                    format(self.room_id, self.player_id, directions))
        except Exception as e:
            print('设置方向错误', e)

    def _update_soliders(self):
        # 21 * 41
        heros = {}
        enemies = {}

        row = len(self.battleground)
        col = len(self.battleground[0])

        for i in range(row):
            for j in range(col):
                p = self.battleground[i][j]
                if not isinstance(p, dict):
                    continue
                if p.get('army_type') == 'q':
                    solider = QSolider(order=p.get('order'), position=(i, j), hp=p.get('hp'),
                                       direction=p.get('direction'), manager=self)
                elif p.get('army_type') == 'g':
                    solider = GSolider(order=p.get('order'), position=(i, j), hp=p.get('hp'),
                                       direction=p.get('direction'), manager=self)
                else:
                    solider = BSolider(order=p.get('order'), position=(i, j), hp=p.get('hp'),
                                       direction=p.get('direction'), manager=self)

                if p.get('player_id') == PLAYER_ID:
                    heros[solider.order] = solider
                else:
                    enemies[solider.order] = solider
        self.heros = heros
        self.enemies = enemies

    def nearlest_enemy(self, solider):
        position = solider.position
        _enemy = None
        near_dis = float('inf')
        for order, enemy in self.enemies.items():
            dis = (position[0] - enemy.position[0])**2 + (position[1] - enemy.position[1])**2
            if dis < near_dis:
                near_dis = dis
                _enemy = enemy
        return _enemy

    def is_wall(self, x, y):
        return self.battleground[x][y] == -1


if __name__ == '__main__':
    manager = Manager(ROOM_ID, PLAYER_ID, POSITION)
    manager.reset_room()
    if manager.enter_room(INFORMATION):
        manager.start()



