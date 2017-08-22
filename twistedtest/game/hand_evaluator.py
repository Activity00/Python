def get_best_hand(hand):
    # 1 花色和数字分离
    split_hand = [(c[0], int(c[1:])) for c in hand]
    
    # 2 形成牌结构
    # 牌结构，记录每个花色几张，每个数字几张，可能的顺子结构，可能的同花结构
    hand_struct = {
        'suits': { 'C': 0, 'D': 0, 'H': 0, 'S': 0 }, # 花色：几张
        'number': { 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0 }, # 数字：几张
        'straight_flush': [], # 最大的同花顺
        'four_of_a_kind': [], # 四条
        'full_house': [], # 葫芦
        'flush': [], # 最大的同花
        'straight': [], # 最大的顺子
        'three_of_a_kind': [], # 三条
        'two_pairs': [], # 两对
        'pair': [], # 对子
        'high_card': [], # 高牌
    }
    
    # 记录每个花色几张，每个数字几张
    for c in split_hand:
        hand_struct['suits'][c[0]] += 1
        hand_struct['number'][c[1]] += 1
    
    # 3 按花色排序，按数字排序
    suit_sorted_hand = sorted(split_hand)
    number_sorted_hand = sorted(split_hand, key=lambda c: (c[1], c[0]))
    
    # 4 找出最大的同花(如果有)，同时找出最大的同花顺(如果有)，没有同花就不会有同花顺
    for suit, suit_count in hand_struct['suits'].items():
        if suit_count >= 5:
            ss = list(filter(lambda c: c[0] == suit, suit_sorted_hand)) # 同花色牌列表
            hand_struct['flush'] = ss[-5:].reverse()
            
            # n张同花，要进行n - 5 + 1次比对，例如7张同花，要进行3次比对
            for i in range(len(ss) - 5 + 1):
                j = len(ss) - i - 1 # 最后的索引值
                if (ss[j][1] - ss[j-1][1]) == 1 and (ss[j-1][1] - ss[j-2][1]) == 1 and \
                    (ss[j-2][1] - ss[j-3][1]) == 1 and (ss[j-3][1] - ss[j-4][1]) == 1:
                    hand_struct['straight_flush'] = [ss[j], ss[j-1], ss[j-2], ss[j-3], ss[j-4]]
                    break
            
            # 特殊处理1,2,3,4,5的同花顺
            if not hand_struct['straight_flush']:
                if [ss[0][1], ss[1][1], ss[2][1], ss[3][1], ss[-1][1]] == [2, 3, 4, 5, 14]:
                    hand_struct['straight_flush'] = [ss[-1], ss[0], ss[1], ss[2], ss[3]]
                    
            break
        
    # 5 找出最大的顺子(如果有)
    n_set = set() # 数字集合
    ns = [] # 去重数字牌列表
    for i in range(len(number_sorted_hand) - 1, -1, -1):
        c = number_sorted_hand[i]
        if c[1] not in n_set:
            n_set.add(c[1])
            ns.append(c)
    ns.reverse()
            
    if len(ns) >= 5:
        # n张同花，要进行n - 5 + 1次比对，例如7张同花，要进行3次比对
        for i in range(len(ns) - 5 + 1):
            j = len(ns) - i - 1 # 最后的索引值
            if (ns[j][1] - ns[j-1][1]) == 1 and (ns[j-1][1] - ns[j-2][1]) == 1 and \
                (ns[j-2][1] - ns[j-3][1]) == 1 and (ns[j-3][1] - ns[j-4][1]) == 1:
                hand_struct['straight'] = [ns[j], ns[j-1], ns[j-2], ns[j-3], ns[j-4]]
                break
            
        # 特殊处理1,2,3,4,5的顺子
        if not hand_struct['straight']:
            if [ns[0][1], ns[1][1], ns[2][1], ns[3][1], ns[-1][1]] == [2, 3, 4, 5, 14]:
                hand_struct['straight'] = [ns[-1], ns[0], ns[1], ns[2], ns[3]]
                
    # 6 高牌，对子，两对，三条，葫芦，四条检查
    cn = [] # (牌数, 数字)
    for n, c in hand_struct['number'].items():
        if c > 1:
            cn.append((c, n))
    cn.sort()
            
    if not cn: # 高牌
        high_card_hand = number_sorted_hand[-5:]
        high_card_hand.reverse()
        hand_struct['high_card'] = high_card_hand
    else:
        if cn[-1][0] == 4: # 四条
            for c in number_sorted_hand:
                if c[1] == cn[-1][1]:
                    hand_struct['four_of_a_kind'].append(c)
            for i in range(len(number_sorted_hand) - 1, -1, -1):
                c = number_sorted_hand[i]
                if c[1] != cn[-1][1]:
                    hand_struct['four_of_a_kind'].append(c)
                    break
        elif cn[-1][0] == 3 and len(cn) >= 2: # 葫芦
            for c in number_sorted_hand:
                if c[1] == cn[-1][1]:
                    hand_struct['full_house'].append(c)
            for c in number_sorted_hand:
                if c[1] == cn[-2][1]:
                    hand_struct['full_house'].append(c)
                    if len(hand_struct['full_house']) == 5:
                        break
        elif cn[-1][0] == 3 and len(cn) == 1: # 三条
            for c in number_sorted_hand:
                if c[1] == cn[-1][1]:
                    hand_struct['three_of_a_kind'].append(c)
            for i in range(len(number_sorted_hand) - 1, -1, -1):
                c = number_sorted_hand[i]
                if c[1] != cn[-1][1]:
                    hand_struct['three_of_a_kind'].append(c)
                    if len(hand_struct['three_of_a_kind']) == 5:
                        break
        elif cn[-1][0] == 2 and len(cn) >= 2: # 两对
            for c in number_sorted_hand:
                if c[1] == cn[-1][1]:
                    hand_struct['two_pairs'].append(c)
            for c in number_sorted_hand:
                if c[1] == cn[-2][1]:
                    hand_struct['two_pairs'].append(c)
                    if len(hand_struct['two_pairs']) == 4:
                        break
            for i in range(len(number_sorted_hand) - 1, -1, -1):
                c = number_sorted_hand[i]
                if c[1] != cn[-1][1] and c[1] != cn[-2][1]:
                    hand_struct['two_pairs'].append(c)
                    break
        elif cn[-1][0] == 2 and len(cn) == 1: # 一对
            for c in number_sorted_hand:
                if c[1] == cn[-1][1]:
                    hand_struct['pair'].append(c)
            for i in range(len(number_sorted_hand) - 1, -1, -1):
                c = number_sorted_hand[i]
                if c[1] != cn[-1][1]:
                    hand_struct['pair'].append(c)
                    if len(hand_struct['pair']) == 5:
                        break
            
    for hand_type in ['straight_flush', 'four_of_a_kind', 'full_house', 'flush', 'straight', \
                      'three_of_a_kind', 'two_pairs', 'pair', 'high_card']:
        if hand_struct[hand_type]:
            if hand_type == 'straight_flush' and hand_struct[hand_type][-1][1] == 14:
                return 'royal_flush', hand_struct[hand_type]
            else:
                return hand_type, hand_struct[hand_type]

def calculate_hand(hand):
    '''
    1. 重新组织牌的结构
    2. 按牌型从高到低判断是否满足，并给出牌型分和大小分：
        2.1 牌型分，高牌，对子，两对，三条，顺子，同花，葫芦，四条，同花顺，皇家同花顺，1到10分
        2.2 大小分，第一决定因素，牌大小*10000，第二决定因素，牌大小*1000，如此类推
        2.3 综合分 = 牌型分 * 1000000 + 大小分
    3. 返回牌型，牌，综合分
    '''
    hand_type, hand_cards = get_best_hand(hand)
    type_score = 10 - ['royal_flush', 'straight_flush', 'four_of_a_kind', 'full_house', 'flush', \
        'straight', 'three_of_a_kind', 'two_pairs', 'pair', 'high_card'].index(hand_type)
    if hand_type == 'royal_flush':
        hand_score = 14 * 10000
    elif hand_type == 'straight_flush':
        hand_score = hand_cards[0][1] * 10000
    elif hand_type == 'four_of_a_kind':
        hand_score = hand_cards[0][1] * 10000 + hand_cards[4][1] * 1000
    elif hand_type == 'full_house':
        hand_score = hand_cards[0][1] * 10000 + hand_cards[3][1] * 1000
    elif hand_type == 'flush':
        hand_score = hand_cards[0][1] * 10000 + hand_cards[1][1] * 1000 + hand_cards[2][1] * 100 \
            + hand_cards[3][1] * 10 + hand_cards[4][1] * 10
    elif hand_type == 'straight':
        hand_score = hand_cards[0][1] * 10000
    elif hand_type == 'three_of_a_kind':
        hand_score = hand_cards[0][1] * 10000 + hand_cards[3][1] * 1000 + hand_cards[2][1] * 100
    elif hand_type == 'two_pairs':
        hand_score = hand_cards[0][1] * 10000 + hand_cards[2][1] * 1000 + hand_cards[4][1] * 100
    elif hand_type == 'pair':
        hand_score = hand_cards[0][1] * 10000 + hand_cards[2][1] * 1000 + hand_cards[3][1] * 100 \
            + hand_cards[4][1] * 10
    elif hand_type == 'high_card':
        hand_score = hand_cards[0][1] * 10000 + hand_cards[1][1] * 1000 + hand_cards[2][1] * 100 \
            + hand_cards[3][1] * 10 + hand_cards[4][1] * 10
            
    result_score = type_score * 1000000 + hand_score

    return hand_type, [c[0] + str(c[1]) for c in hand_cards], result_score


def compare_hands(hands):
    '''
    1. 7选5，选出最好的牌型，得到结果(牌型，选择牌，综合分)，具体说明看该函数
    2. 根据原来列表顺序，返回结果[(牌型，选择牌，综合分), ...]
    '''
    calculate_results = []
    for hand in hands:
        hand_type, hand_cards, result_score = calculate_hand(hand)
        calculate_results.append([hand_type, hand_cards, result_score])
        
    return calculate_results
