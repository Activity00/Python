"""

* 游戏说明
若干玩家进入游戏，根据玩家人数和玩家行动顺序，自动均匀分布到棋盘上面的指定位置。
游戏开始后，会在棋盘上面的所有空格产生1到9的数字，玩家移动到某一格子则获取该格子分数。
游戏每2.4秒为一个回合，玩家在该2.4秒内，获取棋盘情况，设置下一步怎么走。同一回合只能设置一次，可以通过step来判断。
回合结束，所有玩家按顺序移动。如果玩家移动非法，则不移动。
为更好了解游戏机制，以下为一个例子，时间线是为了方便理解：
时间线      执行者      行为            结果
0          管理员      开始游戏         开始游戏
0.5        玩家1       获取房间信息     返回房间信息
0.6        玩家2       获取房间信息     返回房间信息
0.8        玩家2       设置下一步       设置成功
1.0        玩家1       设置下一步       设置成功
1.3        玩家2       设置下一步       设置失败（同一步只能设置一次）
2.4        系统        下一回合         移动玩家1，移动玩家2（假设顺序为1，2）
...


比赛用游戏指令：
1. 加入房间指令：
http://shapan.test01.aragoncs.cn/join-room/?room_id=1&player_id=1&order=0&key=1
room_id：房间号，整数
player_id：玩家id，整数
order：顺序，0-25，整数
key：防伪串，随意字符串
测试阶段随意指定

成功返回：
{"success": true, "message": ""}

失败返回：
{"success": false, "message": "错误信息"}

2. 获取房间信息指令
http://shapan.test01.aragoncs.cn/get-room-info/?room_id=1
room_id：房间号，整数

成功返回：
{
  "players": [{"mark": "A", "player_id": 1, "order": 0, "score": 4}], # 玩家列表，标志，id，顺序，得分
  "state": "over", # 房间状态，waiting/playing/over
  "step": 28, # 回合数，用来判断是否进入下一回合
  "last_step_time": 1566380761.0646675, # 上一回合时间
  "server_time": 1566380763.595813, # 当前服务器时间，与上一回合时间相减，可以知道下一个指令该什么时间发
  "ground": [] # 19 * 19矩阵，如果是数字，则可以移动，如果是字母，则为玩家
}

失败出错

3. 设置下一步
http://shapan.test01.aragoncs.cn/set-direction/?room_id=1&player_id=1&direction=0&key=1
room_id：房间号，整数
player_id：玩家id，整数
direction：方向，0-7，整数。依次为，上，右上，右，右下，下，左下，左，左上
key：防伪串，随意字符串，与加入房间时一致

成功返回：
{"success": true, "message": ""}

失败返回：
{"success": false, "message": "错误信息"}


测试用游戏指令：
4. 开始游戏
http://shapan.test01.aragoncs.cn/start-room/?room_id=1

5. 重置游戏
http://shapan.test01.aragoncs.cn/reset-room/?room_id=1
直接把房间干掉，重新整个流程

6. 旁观游戏
http://shapan.test01.aragoncs.cn/watch-room/?room_id=1
测试用，简陋的UI
"""
import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
