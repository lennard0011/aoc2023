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

    while (not all([current_node in end_nodes for current_node in current_nodes])):
        # check all current_nodes. If they are an end node, remove them from the list and add the cycle.

        direction = directions[direction_index % len(directions)]
        current_nodes = [route_map[current_node][0] if direction == 'L' else route_map[current_node][1] for current_node in current_nodes]
        direction_index += 1
    print(direction_index)
        

# 251553405 too high

run(1, 'input')