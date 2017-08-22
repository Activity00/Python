from texas.game.deck import Deck
from texas.game.hand_evaluator import compare_hands

class PlayerState(object):
    def __init__(self, player_id, position, stack):
        # 进入游戏的玩家状态，可能的状态为：
        # waiting: 未行动
        # small-blind, big-blind: 小盲，大盲
        # check, bet, raise, call, fold: 对应游戏行动
        # all-in: all-in
        self.state = 'waiting'
        
        self.player_id = player_id
        self.position = position
        self.stack = stack # 筹码数量
        self.hole_cards = [] # 底牌
        self.hand = []


class GameState(object):
    def __init__(self, max_position_count):
        self.state = 'init'
        
        self.limit = 0 # 底注
        
        self.pot = 0 # 底池
        # 边池，[[筹码数量，[相关玩家位置]]]
        # 在没形成边池前，边池中含有一个伪边池，是跟所有人相关的，即底池
        self.side_pot = []
        
        self.round_bet = {} # 当轮下注
        self.open = False # 是否已经开注
        self.round_all_in = [] # 当轮all-in
        
        self.max_position_count = max_position_count # 最大位置数量
        self.active_player_count = 0 # 活跃玩家数量
        self.active_player_positions = [] # 活跃玩家位置列表，活跃玩家指的参与了当前回合游戏的玩家
        self.fold_player_positions = [] # 弃牌玩家位置列表
        
        # 活跃玩家状态
        self.active_players = []
        
        self.dealer_position = -1 # dealer位置
        self.small_blind_position = -1 # 小盲位置
        self.big_blind_position = -1 # 大盲位置
        self.current_position = -1 # 当前玩家位置
        self.is_new_round = False

        self.deck = Deck()
        
        self.flop_cards = []
        self.turn_card = []
        self.river_card = []
        self.community_cards = []
        self.final_players = []
        self.win_players = []
        
    # 获取没有弃牌的活跃玩家的位置
    def get_left_player_positions(self):
        left_player_positions = []
        for player in self.active_players:
            if player.state != 'fold':
                left_player_positions.append(player.position)
        return left_player_positions
    
    # 获取当前回合剩余玩家的位置，包含当前回合all-in的玩家，不包含fold的和之前all-in的玩家
    def get_current_round_left_player_positions(self):
        current_round_bet_player_positions = []
        for player in self.active_players:
            if player.state == 'fold':
                continue
            elif player.state == 'all-in':
                if player.position in self.round_all_in:
                    current_round_bet_player_positions.append(player.position)
                else:
                    continue
            else:
                current_round_bet_player_positions.append(player.position)
        return current_round_bet_player_positions

    # 获取当前回合弃牌的活跃玩家的位置
    def get_fold_player_positions(self):
        fold_player_positions = []
        for player in self.active_players:
            if player.state == 'fold':
                fold_player_positions.append(player.position)
        return fold_player_positions
    
    # 获取指定位置玩家
    def get_player_at_position(self, position):
        if position in self.active_player_positions:
            return self.active_players[self.active_player_positions.index(position)]
        else:
            return None
    
    # 重置游戏状态，玩家数据基本上需要保留
    def reset_state(self):
        self.state = 'init'
        
        self.pot = 0
        self.side_pot = []
        self.round_bet = {}
        self.open = False
        self.round_all_in = []

        self.is_new_round = False

        self.deck = Deck()
        self.flop_cards = []
        self.turn_card = []
        self.river_card = []
        self.community_cards = []
        self.final_players = []
        self.win_players = []
        
    def get_available_actions(self):
        current_index = self.active_player_positions.index(self.current_position)
        current_player = self.active_players[current_index]
        
        if self.open:
            max_round_bet = max(self.round_bet.values())
        else:
            max_round_bet = 0
        
        available_actions = []
        if not self.open:
            available_actions = ['check', 'bet', 'fold', 'all-in']
        else:
            if current_player.state == 'big-blind':
                if max_round_bet == self.round_bet[current_player.position]:
                    available_actions = ['check', 'raise', 'fold', 'all-in']
                else:
                    available_actions = ['call', 'raise', 'fold', 'all-in']
            else:
                available_actions = ['call', 'raise', 'fold', 'all-in']
            
        for i in range(len(available_actions) - 1, -1, -1):
            action = available_actions[i]
            if action in ['check', 'fold', 'all-in']:
                continue
            elif action == 'bet':
                if current_player.stack < self.limit:
                    available_actions.pop(i)
            elif action == 'call':
                if current_player.stack + self.round_bet.get(current_player.position, 0) < max_round_bet:
                    available_actions.pop(i)
            elif action == 'raise':
                if current_player.stack + self.round_bet.get(current_player.position, 0) - max_round_bet < self.limit:
                    available_actions.pop(i)
        
        return available_actions

    def deal(self):
        hole_card_list = self.deck.deal(len(self.active_player_positions))
        for i in range(self.active_player_count):
            self.active_players[(self.active_player_positions.index(self.dealer_position) + i + 1) % self.active_player_count].hole_cards = \
                hole_card_list[i]
    
    def start(self, players, limit=20):
        if self.state != 'init':
            return False, '当前游戏状态不对'
        
        if len(players.keys()) < 2:
            return False, '至少2个玩家'
        
        if not all([player.stack for player in players.values()]):
            return False, '至少一名玩家持有筹码不足'
        
        self.state = 'preflop'
        self.limit = limit
        
        self.active_player_positions = sorted(players.keys())
        self.active_player_count = len(self.active_player_positions)
        self.active_players = []
        for i in self.active_player_positions:
            for position, player in players.items():
                if position == i:
                    self.active_players.append(PlayerState(player.player_id, position, player.stack))
                    break
        
        while True:
            self.dealer_position = (self.dealer_position + 1) % self.max_position_count
            if self.dealer_position in self.active_player_positions:
                break
        
        if self.active_player_count > 2:
            self.small_blind_position = self.active_player_positions[
                (self.active_player_positions.index(self.dealer_position) + 1) % \
                self.active_player_count]
            self.big_blind_position = self.active_player_positions[
                (self.active_player_positions.index(self.dealer_position) + 2) % \
                self.active_player_count]
        else:
            self.small_blind_position = self.dealer_position
            self.big_blind_position = self.active_player_positions[
                (self.active_player_positions.index(self.dealer_position) + 1) % \
                self.active_player_count]
            
        self.open = True
        
        # 小盲下注。足够，下注，不够，标注all-in
        small_blind_player = self.active_players[self.active_player_positions.index(self.small_blind_position)]
        if small_blind_player.stack >= self.limit // 2:
            self.round_bet[self.small_blind_position] = self.limit // 2
            small_blind_player.stack -= self.limit // 2
            small_blind_player.state = 'small-blind'
        else:
            self.round_bet[self.small_blind_position] = small_blind_player.stack
            small_blind_player.stack = 0
            small_blind_player.state = 'all-in'
            self.round_all_in.append(self.small_blind_position)
        
        # 大盲下注。足够，下注，不够，标注all-in
        big_blind_player = self.active_players[self.active_player_positions.index(self.big_blind_position)]
        if big_blind_player.stack >= self.limit:
            self.round_bet[self.big_blind_position] = self.limit
            big_blind_player.stack -= self.limit
            big_blind_player.state = 'big-blind'
        else:
            self.round_bet[self.big_blind_position] = big_blind_player.stack
            big_blind_player.stack = 0
            big_blind_player.state = 'all-in'
            self.round_all_in.append(self.big_blind_position)

        self.deal()
        self.current_position = self.get_next_position(self.big_blind_position)

        return True, None
        
    def has_matched_in_round_bet(self):
        if len(self.get_current_round_left_player_positions()) == len(self.round_all_in):
            return True
        
        if len(self.get_current_round_left_player_positions()) != len(self.round_bet):
            return False
        
        round_bet = self.round_bet.copy()
        max_round_bet = max(round_bet.values())
        
        for position in self.active_player_positions:
            player = self.get_player_at_position(position)
            if player.state in ['small-blind', 'big-blind']:
                return False
            elif player.state == 'fold':
                round_bet.pop(position, None)
            elif player.state == 'all-in':
                round_bet.pop(position, None)
                
        round_bet_list = list(round_bet.values())

        return round_bet_list.count(max_round_bet) == len(round_bet_list)

    def call(self, position):
        is_current = self.is_current_position(position)
        if not is_current:
            return False, '不是当前玩家， 不能执行指令'

        actions = self.get_available_actions()
        if 'call' not in actions:
            return False, '该指令不可用'
        player = self.get_player_at_position(position)

        if not self.check_can_put_in(player.stack, self.get_to_call()):
            return False, '金额不足'

        last_bet = self.round_bet.get(position, 0)
        player.stack -= (self.get_to_call() - last_bet)
        self.round_bet[position] = self.get_to_call()
        player.state = 'call'

        self.current_position = self.get_next_position(position)
        return True, None

    def all_in(self, position):
        is_current = self.is_current_position(position)
        if not is_current:
            return False, '不是当前玩家， 不能执行指令'

        self.open = True
        player = self.get_player_at_position(position)
        if position not in self.round_bet:
            self.round_bet[position] = 0
        self.round_bet[position] += player.stack
        self.round_all_in.append(position)
        player.stack = 0
        player.state = 'all-in'

        self.current_position = self.get_next_position(position)
        return True, None

    def get_to_call(self):
        return max(self.round_bet.values())

    def get_to_raise(self):
        return self.get_to_call() + self.limit

    def bet(self, position, chips):
        is_current = self.is_current_position(position)
        if not is_current:
            return False, '不是当前玩家， 不能执行指令'

        actions = self.get_available_actions()
        if 'bet' not in actions:
            return False, '该指令不可用'
        self.open = True
        player = self.get_player_at_position(position)
        if not self.check_can_put_in(player.stack, chips):
            return False, '金额不足'

        player.stack -= chips
        self.round_bet[position] = chips
        player.state = 'bet'

        self.current_position = self.get_next_position(position)
        return True, None

    def check(self, position):
        is_current = self.is_current_position(position)
        if not is_current:
            return False, '不是当前玩家， 不能执行指令'

        actions = self.get_available_actions()
        if 'check' not in actions:
            return False, '该指令不可用'

        player = self.get_player_at_position(position)
        player.state = 'check'
        if position not in self.round_bet:
            self.round_bet[position] = 0
        self.round_bet[position] += 0

        self.current_position = self.get_next_position(position)
        return True, None

    def raise_chips(self, position, chips):
        is_current = self.is_current_position(position)
        if not is_current:
            return False, '不是当前玩家， 不能执行指令'

        actions = self.get_available_actions()
        if 'raise' not in actions:
            return False, '该指令不可用'
        player = self.get_player_at_position(position)
        if not self.check_can_put_in(player.stack, chips):
            return False, '金额不足'

        player.stack -= chips
        if position not in self.round_bet:
            self.round_bet[position] = 0
        self.round_bet[position] += chips
        player.state = 'raise'

        self.current_position = self.get_next_position(position)
        return True, None

    def fold(self, position):
        is_current = self.is_current_position(position)
        if not is_current:
            return False, '不是当前玩家， 不能执行指令'

        player = self.get_player_at_position(position)
        player.state = 'fold'

        self.current_position = self.get_next_position(position)
        return True, None

    def check_can_build_new_round(self):
        if self.round_bet:
            result = self.has_matched_in_round_bet()
        else:
            if self.current_position == None:
                result = True
            else:
                result = False
        # TODO 建立新的state
        if result:
            if self.state != 'river':
                self.is_new_round = True
                self.put_chips_to_pot()
                self.build_new_round()
            else:
                self.is_new_round = False
                self.state = 'over'
                self.put_chips_to_pot()
                self.showdown()
        else:
            self.is_new_round = False

    def get_next_position(self, position):
        position_index = self.active_player_positions.index(position)
        next_index = (position_index + 1) % self.active_player_count
        while next_index != position_index:
            next_position = self.active_player_positions[next_index]
            next_player = self.get_player_at_position(next_position)
            if next_player.state not in ['fold', 'all-in']:
                return next_position
            next_index = (next_index + 1) % self.active_player_count
        return None

    def build_new_round(self):
        if self.state == 'preflop':
            self.state = 'flop'
            self.flop_cards = self.deck.flop()
        elif self.state == 'flop':
            self.state = 'turn'
            self.turn_card = self.deck.turn()
        elif self.state == 'turn':
            self.state = 'river'
            self.river_card = self.deck.river()
        self.round_bet.clear()
        self.round_all_in.clear()
        self.open = False
        if len(self.get_current_round_left_player_positions()) == 1:
            self.current_position = None
        else:
            self.current_position = self.get_next_position(self.dealer_position)

    def get_community_cards(self):
        community_cards = []
        community_cards.extend(self.flop_cards)
        community_cards.extend(self.turn_card)
        community_cards.extend(self.river_card)
        return community_cards

    def showdown(self):
        
        player_hands = []
        final_players = []

        # 对所有剩余玩家，组装公共牌
        self.community_cards = self.get_community_cards()
        for player in self.active_players:
            if player.state != 'fold':
                hand = []
                hand.extend(player.hole_cards)
                hand.extend(self.community_cards)
                player_hands.append(hand)
                final_players.append(player)
                
        # 计算各玩家手牌得分
        calculate_result = compare_hands(player_hands)
        hand_score_list = []
        for index, player in enumerate(final_players):
            player.hand = calculate_result[index]
            hand_score_list.append(calculate_result[index][2])

        # 按手牌得分从高到底排序
        final_players.sort(key=lambda player: player.hand[2], reverse=True)
        self.final_players = final_players
        hand_score_list.sort(reverse=True)
        
        # 如果没有形成边池，形成一个边池，这样把有边池和没有边池的分法统一处理
        if not self.side_pot:
            self.side_pot.append([self.pot, [player.position for player in final_players]])

        if self.side_pot[-1][0] == 0:
            self.side_pot.pop()
        
        win_players = {} # 获胜玩家位置: 获胜筹码
        left_final_players = final_players.copy()
        while self.side_pot:
            same_score_count = hand_score_list.count(hand_score_list[0])
            if same_score_count > 1:
                same_score_players = left_final_players[:same_score_count]
                left_pot = 0 # 剩余筹码，多人分边池时，有可能会出现分不干净的情况
                # 最后一次与边池有关的玩家。当本次玩家与最后一次玩家不同时，计算剩余筹码
                last_in_side_pot_players = [] 
                while self.side_pot:
                    # 把同分用户分成两部分，与当前边池有关的和与当前边池无关的
                    current_side_pot = self.side_pot[0]
                    in_side_pot_players = []
                    for player in same_score_players:
                        if player.position in current_side_pot[1]:
                            in_side_pot_players.append(player)
                    
                    # 当本次玩家与最后一次玩家不同时，计算剩余筹码
                    if in_side_pot_players != last_in_side_pot_players and left_pot != 0:
                        left_pot_adjust_index = self.active_player_positions.index(self.small_blind_position)
                        while left_pot > 0:
                            left_pot_adjust_position = self.active_player_positions[left_pot_adjust_index]
                            for player in last_in_side_pot_players:
                                if player.position == left_pot_adjust_position:
                                    win_players[player.position] += 1
                                    left_pot -= 1
                                    break
                            left_pot_adjust_index = (left_pot_adjust_index + 1) % self.active_player_count
                    
                    last_in_side_pot_players = in_side_pot_players.copy()
                    
                    # 如果存在与当前边池有关的，给他们分钱
                    if in_side_pot_players:
                        left_pot += current_side_pot[0] % len(in_side_pot_players)
                        for player in in_side_pot_players:
                            if player.position not in win_players:
                                win_players[player.position] = 0
                            win_players[player.position] += current_side_pot[0] // len(in_side_pot_players)
                        self.side_pot.pop(0)
                    else:
                        for _ in range(same_score_count):
                            left_final_players.pop(0)
                            hand_score_list.pop(0)
                        break
            else:
                player = left_final_players[0]
                while self.side_pot:
                    current_side_pot = self.side_pot[0]
                    # 看看用户是否跟当前边池有关。有关，加钱，无关，继续
                    if player.position in current_side_pot[1]:
                        if player.position not in win_players:
                            win_players[player.position] = 0
                        
                        win_players[player.position] += current_side_pot[0]
                        self.side_pot.pop(0)
                    else:
                        left_final_players.pop(0)
                        hand_score_list.pop(0)
                        break

        for position, win_pot in win_players.items():
            player = self.get_player_at_position(position)
            player.stack += win_pot
            self.win_players.append([player, win_pot])

        self.win_players.sort(key=lambda o: o[0].hand[2], reverse=True)

    def check_only_one_player(self):
        if len(self.active_player_positions) - len(self.get_fold_player_positions()) == 1:
            self.state = 'over'
            last_player_position = list(set(self.active_player_positions) - set(self.get_fold_player_positions()))[0]
            last_player = self.active_players[self.active_player_positions.index(last_player_position)]
            self.put_chips_to_pot()
            last_player.stack += self.pot
            self.final_players = [last_player]
            self.win_players = [[last_player, self.pot]]
            self.pot = 0
            return True
        return False

    def check_can_put_in(self, stack, chips):
        return stack >= chips

    def put_chips_to_pot(self):
        # 如果当轮有all in的，形成边池
        if self.round_all_in:
            left_player_positions = self.get_current_round_left_player_positions()
            
            # 边池没形成，初始化边池，初始值为截止上一轮的底池数量，相关玩家为当轮剩余玩家
            if not self.side_pot:
                self.side_pot.append([self.pot, left_player_positions.copy()])
                
            # 当前边池为最后一个边池
            current_side_pot = self.side_pot[-1]
            
            # 排序当轮all-in数量，从小到大形成边池
            round_all_in_bet = [] # 当轮all-in数量，[[位置，下注额]]
            for p in self.round_all_in:
                round_all_in_bet.append([p, self.round_bet[p]])
            round_all_in_bet.sort(key=lambda o: o[1])
            
            last_all_in_bet = 0
            for i, (all_in_position, all_in_bet) in enumerate(round_all_in_bet):
                # 当前all-in数量与最后一个all-in数量不同，则会形成新的边池
                # 把当前的all-in玩家处理完后，又会对其余玩家形成一个新的边池
                if all_in_bet != last_all_in_bet:
                    delta_all_in_bet = all_in_bet - last_all_in_bet
                    for position, bet in self.round_bet.items():
                        if bet >= delta_all_in_bet:
                            current_side_pot[0] += delta_all_in_bet
                            self.pot += delta_all_in_bet
                            self.round_bet[position] -= delta_all_in_bet
                        else:
                            current_side_pot[0] += bet
                            self.pot += bet
                            self.round_bet[position] -= bet
                            
                    left_player_positions.remove(all_in_position)
                    if left_player_positions:
                        self.side_pot.append([0, left_player_positions.copy()])
                        current_side_pot = self.side_pot[-1]
                else: # 当前all-in数量与最后一个all-in数量相同，拼入上一个边池，当前边池移掉他
                    left_player_positions.remove(all_in_position)
                    current_side_pot[1].remove(all_in_position)

                last_all_in_bet = all_in_bet
                
            # 处理完all-in的，剩下的放入最后一个边池，这个边池是在上面过程中创建上的
            self.pot += sum(self.round_bet.values())
            current_side_pot[0] += sum(self.round_bet.values())
        else: # 当轮没有人all-in
            self.pot += sum(self.round_bet.values())
            if self.side_pot: # 如果已经形成了边池，当轮加入最后一个边池
                self.side_pot[-1][0] += sum(self.round_bet.values())

    def is_current_position(self, position):
        return position == self.current_position

