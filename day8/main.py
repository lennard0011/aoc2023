import math

def find_lcm_of_list(numbers):
    if not numbers:
        return None
    
    lcm = numbers[0]
    
    for i in range(1, len(numbers)):
        lcm = lcm * numbers[i] // math.gcd(lcm, numbers[i])
    
    return lcm

def parse_children_string(children_string):
    [left, right] = children_string.replace("(", "").replace(")", "").split(", ")
    return left, right

def run(part=1, file='test'):
    with open(f'day8/{file}.txt') as f:
        lines = f.readlines()
    [directions, _, *nodes] = lines

    directions = directions.replace('\n', '')
    
    route_map = {}
    for node in nodes:
        [parent, children_strings] = node.replace('\n', '').split(' = ')
        left, right = parse_children_string(children_strings)
        route_map[parent] = [left, right]

    current_nodes = [node for node in route_map.keys() if node.endswith('A')] if part == 2 else ['AAA']
    end_nodes = [node for node in route_map.keys() if node.endswith('Z')] if part == 2 else ['ZZZ']

    direction_index = 0

    cycle_lengths = []

    while (len(current_nodes) > 0 and not all([current_node in end_nodes for current_node in current_nodes])):
        direction = directions[direction_index % len(directions)]
        current_nodes = [route_map[current_node][0] if direction == 'L' else route_map[current_node][1] for current_node in current_nodes]
        direction_index += 1

        if part == 2:
            finished_nodes = [current_node for current_node in current_nodes if current_node in end_nodes]
            current_nodes = [current_node for current_node in current_nodes if current_node not in end_nodes]
            cycle_lengths.extend([direction_index for _ in range(len(finished_nodes))])

    if part == 2:
        print(cycle_lengths)
        answer = find_lcm_of_list(cycle_lengths)
        print('steps:', answer)
    if part == 1:
        print('steps', direction_index)
        

# 251553405 too high
# part 2: 147826826783 too low  
#         11678319315857

run(2, 'input')