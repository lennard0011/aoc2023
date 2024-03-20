def format_counters(counters_line):
    counters = [int(counter) for counter in counters_line.split(',')]
    return counters

def get_sequences(line):
    sequences = [len(seq) for seq in line.split('.') if '#' in seq]
    return sequences

def get_options(puzzle):
    solutions = []
    if '?' not in puzzle:
        return [puzzle]
    for i in range(len(puzzle)):
        if puzzle[i] != '?':
            continue
        new_dot_solution = puzzle[:i] + '.' + puzzle[i+1:]
        dot_solutions = get_options(new_dot_solution)
        new_sharp_solution = puzzle[:i] + '#' + puzzle[i+1:]
        sharp_solutions = get_options(new_sharp_solution)
        solutions += dot_solutions + sharp_solutions
        break
    return solutions

def verify_solution(puzzle, counters):
    sequences = get_sequences(puzzle)
    return sequences == counters

def get_number_of_options(line):
    [puzzle, counters] = line.split(' ')
    counters = format_counters(counters)
    options = get_options(puzzle)
    valid_options = [option for option in options if verify_solution(option, counters)]
    return len(valid_options)

def run(part=1, file='test'):
    with open(f'day12/{file}.txt') as f:
        lines = f.readlines()

    number_of_options = 0

    count = 0
    for line in lines:
        line = line.strip('\n')
        number_of_options += get_number_of_options(line)
        count += 1
        print(count, number_of_options)
    print(number_of_options)

run(1, 'input')