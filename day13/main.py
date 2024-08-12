def split_on_empty_lines(lines): 
    puzzles = []
    current_puzzle=[]
    for line in lines:
        if line == "":
            puzzles.append(current_puzzle)
            current_puzzle = []
        else:
            current_puzzle.append(line)
    puzzles.append(current_puzzle)
    return puzzles

def get_vertical_mirror(puzzle):
    return 0

def check_horizontal_mirror_on(puzzle, index):
    number_of_rows = len(puzzle)
    number_of_rows_to_check = min()
    return False


def get_horizontal_mirror(puzzle):
    number_of_rows = len(puzzle)
    for index in range(number_of_rows - 1):
        is_match = check_horizontal_mirror_on(puzzle, index)
        if (is_match):
            return index
    return -1
    

def solve_puzzle(puzzle):
    horizontal_match = get_horizontal_mirror(puzzle)
    if horizontal_match != -1:
        return horizontal_match
    vertical_match = get_vertical_mirror(puzzle)
    if vertical_match != -1:
        return vertical_match
    raise Exception('puzzle not solved')


def run(part=1, file='test'):
    with open(f'day13/{file}.txt') as f:
        lines = [line.strip('\n') for line in f.readlines()]
    
    puzzles = split_on_empty_lines(lines)

    result = 0

    for puzzle in puzzles:
        result += solve_puzzle(puzzle)

    print('The result is ', result)


run() 