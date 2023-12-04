import re


def format_numbers_to_list(numbers_string):
    numbers_list = [number for number in numbers_string.split(' ') if number != '']
    return [int(number) for number in numbers_list]

def get_score_based_on_len(amount_of_winning_numbers):
    if amount_of_winning_numbers == 0:
        return 0
    return pow(2, amount_of_winning_numbers-1)


def get_game_id_to_winning_numbers(mapping, game_id, game_id_to_winning_numbers):
    if game_id in mapping:
        return mapping, mapping[game_id]
    if game_id_to_winning_numbers[game_id] == 0:
        mapping[game_id] = 0
        return mapping, 0
    new_game_ids = list(range(game_id+1, game_id+game_id_to_winning_numbers[game_id]+1))
    new_cards_amount = len(new_game_ids)
    for new_game_id in new_game_ids:
        mapping, this_new_cards_amount = get_game_id_to_winning_numbers(mapping, new_game_id, game_id_to_winning_numbers)
        new_cards_amount += this_new_cards_amount
    mapping[game_id] = new_cards_amount
    return mapping, new_cards_amount
    

def run(part=1, file='test'):
    text_file = open(f"./day4/{file}.txt")
    lines = text_file.readlines()

    answer = 0

    game_ids = []
    game_id_to_winning_numbers = {}

    for line in lines:
        line = line.strip('\n')
        [game_string, card_numbers] = line.split(': ')
        game_id = int(re.search(r'\b(\d+)\b', game_string).group(1))
        game_ids.append(game_id)

        [winning_numbers_string, my_numbers_string]  = card_numbers.split(' | ')
        winning_numbers = format_numbers_to_list(winning_numbers_string)
        my_numbers = format_numbers_to_list(my_numbers_string)
        my_winnning_numbers = [number for number in my_numbers if number in winning_numbers]

        game_id_to_winning_numbers[game_id] = len(my_winnning_numbers)

        answer += get_score_based_on_len(len(my_winnning_numbers))
    print('part 1 answer: ', answer)

    if part == 2:
        answer2 = 0
        game_id_to_resulting_cards = {}
        answer2 += len(game_ids)

        for game_id in game_ids:
            game_id_to_resulting_cards, resulting_number_of_cards = get_game_id_to_winning_numbers(game_id_to_resulting_cards, game_id, game_id_to_winning_numbers)
            answer2 += resulting_number_of_cards       
        print('part 2 answer: ', answer2)

    text_file.close()

run(2, 'input')  
