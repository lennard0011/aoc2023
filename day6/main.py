def parse_digits(line):
    return [int(values) for values in line.split(' ') if values.isdigit()]

def parse_digits_joined(line):
    all_digits =  [int(values) for values in line.split(' ') if values.isdigit()]
    total_number = ''
    for digits in all_digits:
        total_number += str(digits)
    return [int(total_number)]        


def parse_game(lines, parse_function):
    games = []
    time = lines[0].replace('\n', '')
    distance = lines[1].replace('\n', '')

    for time, distance in zip(parse_function(time), parse_function(distance)):
        games.append({'time': time, 'distance': distance})
    return games

def find_winning_options(game):
    winning_options = []
    
    for button_press_time in range(0, game['time'] + 1):
        driving_time = game['time'] - button_press_time
        distance = button_press_time * driving_time
        if distance > game['distance']:
            winning_options.append(button_press_time)

    return winning_options

def find_winning_options_many(game):
    summed = game['time']
    multiplied = game['distance']
    step_size = int(summed / 2)
    current_button_time = 0
    prev_button_time = -1
    prev_prev_button_time = -1

    while True:
        current_distance = current_button_time * (summed - current_button_time)
        print(multiplied - current_distance, current_button_time, step_size)
        if current_distance > multiplied:
            current_button_time -= step_size
        else:
            current_button_time += step_size            
        if prev_prev_button_time == current_button_time:
            return current_button_time
        step_size = max(int(step_size * 0.99), 1)
        prev_prev_button_time = prev_button_time
        prev_button_time = current_button_time
        

    # first we are going to find the border place of winning where 


def run(part=1, file='test'):
    with open(f'day6/{file}.txt') as f:
        lines = f.readlines()
    parse_function = parse_digits if part == 1 else parse_digits_joined
    games = parse_game(lines, parse_function)

    possibilities_to_win = 1
    for game in games:
        winning_options = find_winning_options(game) if part == 1 else find_winning_options_many(game)
        possibilities_to_win *= len(winning_options)
        print(len(winning_options))
    print(possibilities_to_win)


run(2, 'input')