hand_to_rank_mapping = {
    'Five of a kind': 7,
    'Four of a kind': 6,
    'Full house': 5,
    'Three of a kind': 4,
    'Two pair': 3,
    'One pair': 2,
    'High card': 1
}

card_to_rank_mapping = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3, 
    '2': 2,
}

card_to_rank_mapping2 = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3, 
    '2': 2,
    'J': 1,
}

def classify_hand(hand_string, joker=None):
    hand_mapping = {}
    joker_count = 0

    for card in hand_string:
        if card == joker:
            joker_count += 1
            continue
        if not card in hand_mapping:
            hand_mapping[card] = 0
        hand_mapping[card] += 1
    
    if max(hand_mapping.values(), default=0) + joker_count == 5:
        return 'Five of a kind'
    if max(hand_mapping.values(), default=0) + joker_count == 4:
        return 'Four of a kind'
    if len(hand_mapping) <= 2:
        return 'Full house'
    elif max(hand_mapping.values(), default=0) + joker_count == 3:
        return 'Three of a kind'
    elif len(hand_mapping) == 3 or (joker_count == 1 and max(hand_mapping.values(), default=0) == 2) or joker_count == 2:
        return 'Two pair'
    elif len(hand_mapping) == 4:
        return 'One pair'
    return 'High card'

class PokerGame:
    def __init__(self, hand_string, bid, joker=None):
        self.hand_string = hand_string
        self.hand = classify_hand(hand_string, joker)
        self.bid = int(bid)
        self.card_ranking = card_to_rank_mapping2 if joker else card_to_rank_mapping

    def __lt__(self, other):
        if hand_to_rank_mapping[self.hand] < hand_to_rank_mapping[other.hand]:
            return True
        if hand_to_rank_mapping[self.hand] > hand_to_rank_mapping[other.hand]:
            return False
        for my_card, other_card in zip(self.hand_string, other.hand_string):
            if self.card_ranking[my_card] < self.card_ranking[other_card]:
                return True
            if self.card_ranking[my_card] > self.card_ranking[other_card]:
                return False
        return False
        


def run(part=1, file='test'):
    joker = 'J' if part == 2 else None
    with open(f'day7/{file}.txt') as f:
        lines = f.readlines()
    poker_games = []
    for hand, bid in [(formatted_line[0], formatted_line[1]) for formatted_line in [line.replace('\n', '').split(' ') for line in lines]]:
        poker_games.append(PokerGame(hand, bid, joker))
    
    poker_games.sort()

    result = 0
    for index, poker_game in enumerate(poker_games):
        result += (index+1) * poker_game.bid
    print(result)

# 251553405 too high

run(2, 'input')