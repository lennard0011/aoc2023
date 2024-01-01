def format_counters(counters_line):
    counters = [int(counter) for counter in counters_line.split(',')]
    return counters

def get_sequences(line):
    sequences = [char if char == '#' else '/n' for char in line]
    return sequences

def get_options(puzzle, counters):
    print(0)

def verify_solution(puzzle, counters):
    get_sequences(puzzle)
    # for every sequence in puzzle, check if the length is correct.

def get_number_of_options(line):
    [puzzle, counters] = line.split('')
    counters = format_counters(counters)
    get_options(puzzle, counters)

def run(part=1, file='test'):
    with open(f'day12/{file}.txt') as f:
        lines = f.readlines()

    number_of_options = 0

    for line in lines:
        number_of_options += get_number_of_options(line)
    print(number_of_options)
