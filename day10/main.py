inverse_direction = {
    'up': 'down',
    'down': 'up',
    'left': 'right',
    'right': 'left'
}

def calculate_area_of_pipe(pipe):
    sum = 0
    shifted_pipe = pipe[1:].copy()
    shifted_pipe.append(pipe[0])
    for pipe_i, pipe_j in zip(pipe, shifted_pipe):
        sum += pipe_i[0] * pipe_j[1] - pipe_i[1] * pipe_j[0]
    return abs(sum / 2)

def calculate_points_in_pipe(pipe, area):
    return int(area - (len(pipe) // 2) + 1)

def find_first_direction(grid, x, y):
    if y > 0:
        if grid[y-1][x] in ['|', '7', 'F']:
            return 'up'
    if y < len(grid) - 1:
        if grid[y+1][x] in ['|', 'L', 'J']:
            return 'down'
    if x > 0:
        if grid[y][x-1] in ['-', 'F', 'L']:
            return 'left'
    if x < len(grid[y]) - 1:
        if grid[y][x+1] in ['-', '7', 'J']:
            return 'right'

def get_next_direction(x, y, grid, coming_from):
    # all_directions = ['up', 'left', 'down', 'right']
    current_pipe = grid[y][x]
    if current_pipe == '|':
        possible_directions = ['up', 'down']
    elif current_pipe == '-':
        possible_directions = ['left', 'right']
    elif current_pipe == 'L':
        possible_directions = ['up', 'right']
    elif current_pipe == 'J':
        possible_directions = ['up', 'left']
    elif current_pipe == '7':
        possible_directions = ['down', 'left']
    elif current_pipe == 'F':
        possible_directions = ['down', 'right']
    else:
        raise Exception(f'Unknown pipe: {current_pipe}')
    next_direction = [direction for direction in possible_directions if direction != coming_from][0]
    return next_direction

def get_next_position(x, y, direction):
    if direction == 'up':
        return x, y-1
    elif direction == 'down':
        return x, y+1
    elif direction == 'left':
        return x-1, y
    elif direction == 'right':
        return x+1, y
    else:
        raise Exception(f'Unknown direction: {direction}')


def run(part=1, file='test'):
    with open(f'day10/{file}.txt') as f:
        lines = f.readlines()

    # Initiate the grid
    grid = []
    for line in lines:
        grid.append(list(line.replace('\n', '')))
    
    # find the starting point
    starting_point = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                starting_point = (x, y)
                break
        if starting_point:
            break

    start_x, start_y = starting_point
    next_direction = find_first_direction(grid, start_x, start_y)
    current_x, current_y = get_next_position(start_x, start_y, next_direction)
    steps = 1

    pipe = [[start_y, start_x]]
    
    while(grid[current_y][current_x] != 'S'):
        pipe.append([current_y, current_x])
        next_direction = get_next_direction(current_x, current_y, grid, inverse_direction[next_direction])
        current_x, current_y = get_next_position(current_x, current_y, next_direction)
        steps += 1
    
    if part == 1:
        answer = int(steps / 2)
    else:
        area = calculate_area_of_pipe(pipe)
        answer = calculate_points_in_pipe(pipe, area)

    print(answer)
    
        
run(2, 'input')