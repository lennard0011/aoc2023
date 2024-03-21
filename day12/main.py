def format_counters(counters_line):
    counters = tuple([int(counter) for counter in counters_line.split(',')])
    return counters

cache = {}

def get_options_v2(puzzle, counters):
    key = (puzzle, counters)
    if key in cache:
        return cache[key]
    
    if puzzle == "":
        return 1 if counters == () else 0
    if counters == ():
        return 0 if "#" in puzzle else 1
    
    options = 0

    if puzzle[0] in ".?":
        options += get_options_v2(puzzle[1:], counters)

    if puzzle[0] in '#?':
        if counters[0] <= len(puzzle) and "." not in puzzle[:counters[0]] and (counters[0] == len(puzzle) or puzzle[counters[0]] != "#"):
            options += get_options_v2(puzzle[counters[0] + 1:], counters[1:])

    cache[key] = options
    
    return options


def get_number_of_options(line, part=1):
    [puzzle, counters] = line.split(' ')
    
    if part == 2:
        puzzle = f"{puzzle}?{puzzle}?{puzzle}?{puzzle}?{puzzle}"
        counters = f"{counters},{counters},{counters},{counters},{counters}"

    counters = format_counters(counters)
    options = get_options_v2(puzzle, counters)
    return options


def run(part=1, file='test'):
    with open(f'day12/{file}.txt') as f:
        lines = f.readlines()

    number_of_options = 0

    for line in lines:
        line = line.strip('\n')
        current_number_of_options = get_number_of_options(line, part)
        number_of_options += current_number_of_options
    print("total solutions: ",number_of_options)

run(2, 'input')