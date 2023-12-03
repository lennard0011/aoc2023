import re

requirement = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

colors = ["red", "green", "blue"]

class Hand: 
    def __init__(self, handLine):
        self.color_values = {}
        self._create_color_values(handLine)

    def _create_color_values(self, handline: str):
        colors_with_values_string = handline.split(", ")
        for color_value_string in colors_with_values_string:
            color_value = color_value_string.split(" ")
            value = int(color_value[0])
            color = color_value[1].strip("\n")
            self.color_values[color] = value

    def check_against_requirements(self, requirements):
        for req_color, req_value in requirements.items():
            if req_color in self.color_values and self.color_values[req_color] > req_value:
                return False
        return True
    
    def get_minimum_gems(self, color_name):
        if color_name in self.color_values:
            return self.color_values[color_name]
        else:
            return 0

class Game:
    def __init__(self, game_line):
        self.id = None
        self.hands = []
        self._create_game(game_line)

    def _create_game(self, game_line):
        [game_id_name, hands_line] = game_line.split(": ")
        
        self.id = int(re.search(r"Game\s+(\d+)", game_id_name).group(1))
        
        hands = hands_line.split("; ")
        for hand_line in hands:
            self.add_hand(hand_line)

    def add_hand(self, hand_line):
        newHand = Hand(hand_line)
        self.hands.append(newHand)

    def hands_fulfills_requirement(self, requirement):
        for hand in self.hands:
            if not hand.check_against_requirements(requirement):
                return False
        return True
    
    def get_id(self):
        return self.id
    
    def fewest_gems_in_hands(self):
        fewest_gem_overview = {}
        for color in colors:
            fewest_gem_amount = 0
            for hand in self.hands:
                fewest_gem_amount = max(fewest_gem_amount, hand.get_minimum_gems(color))
            fewest_gem_overview[color] = fewest_gem_amount
        return fewest_gem_overview
            
    def get_game_power(self):
        fewest_gems = self.fewest_gems_in_hands()
        power = 1
        for color in colors:
            power *= fewest_gems[color]
        return power

def run(part=1, file='test'):
    text_file = open(f"./day2/{file}{part}.txt")
    lines = text_file.readlines()

    answer = 0

    for line in lines:
        current_game = Game(line)
        if (part == 1 and current_game.hands_fulfills_requirement(requirement)):
            answer += current_game.get_id()
        elif (part == 2):
            answer += current_game.get_game_power()
        
    print(answer)
    text_file.close()

run(2, 'input')