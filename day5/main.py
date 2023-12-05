def find_location_of_seed(lines, start_id):
    next_id = None
    for index, line in enumerate(lines):
        if line != '' and line[0].isdigit():
            [dest_start, source_start, range_length] = [int(myString) for myString in line.split(' ')]
            if source_start <= start_id < source_start + range_length:
                current_length = start_id - source_start 
                next_id = dest_start + current_length
        if line == '':
            # new segment
            break
    if next_id is None:
        next_id = start_id
    if index == len(lines) - 1:
        return next_id  
    return find_location_of_seed(lines[index+1:], next_id)

def run(part=1, file='test'):
    with open(f'day5/{file}.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    first_line = lines.pop(0)
    [_, seeds_line] = first_line.split(': ')
    seeds = [int(seed) for seed in seeds_line.split(' ')]
    
    if part == 2:
        new_seed_pairs = []
        while len(seeds) > 0:
            seed_start_pair = seeds.pop(0)
            seed_length_pair = seeds.pop(0)
            new_seed_pairs.extend(list(range(seed_start_pair, seed_start_pair + seed_length_pair)))
        seeds = new_seed_pairs

    lines.pop(0) # remove empty line

    locations = []
    for seed in seeds:
        locations.append(find_location_of_seed(lines, seed))
    
    print('All locations: ', locations)
    print('Lowest location id: ',min(locations))


run(2, 'input')