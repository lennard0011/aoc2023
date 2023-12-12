def get_number(grid, x, y):
    if y >= len(grid):
        return None
    if x >= len(grid[0]):
        return None
    if not grid[y][x].isnumeric():
        return None
    current_number = int(grid[y][x])

    next_number = get_number(grid, x+1, y)
    if next_number is None:
        return current_number
    current_number = str(current_number) + str(next_number)
    return current_number

def is_symbol(char):
    return char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

def is_number(char):
    return char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def has_surrounding_symbols(grid, x, y, length, check_left=True):
    # first check left, then right, then up, then down, then diagonals

    # left
    if x > 0 and check_left:
        if is_symbol(grid[y][x-1]):
            return True
    # right
    if x < len(grid[0])-1 and length == 1:
        if is_symbol(grid[y][x+1]):
            return True
    # up neighbour
    if y > 0:
        if is_symbol(grid[y-1][x]):
            return True
    # down neighbour
    if y < len(grid)-1:
        if is_symbol(grid[y+1][x]):
            return True
        
    # diagonals
    # up left neighbour
    if x > 0 and y > 0:
        if is_symbol(grid[y-1][x-1]):
            return True
    # up right neighbour
    if x < len(grid[0])-1 and y > 0:
        if is_symbol(grid[y-1][x+1]):
            return True
    # down left neighbour
    if x > 0 and y < len(grid)-1:
        if is_symbol(grid[y+1][x-1]):
            return True
    # down right neighbour
    if x < len(grid[0])-1 and y < len(grid)-1:
        if is_symbol(grid[y+1][x+1]):
            return True

    if length > 1:
        # left has already been checked, no need to check it from now on.
        return has_surrounding_symbols(grid, x+1, y, length-1, False)
    return False


def playback_number(grid, x, y):
    # we are going to return the coordinates of the start of the number
    if x == 0:
        return x, y
    if is_number(grid[y][x-1]):
        return playback_number(grid, x-1, y)
    return x, y

def has_two_surrounding_numbers_and_returns(grid, x, y):
    # first check left, then right, then up, then down, then diagonals
    numbers_coordinates = []    
    has_up_mid = False
    has_down_mid = False

    # left
    if x > 0:
        if is_number(grid[y][x-1]):
            numbers_coordinates.append([x-1, y])
    # right
    if x < len(grid[0])-1:
        if is_number(grid[y][x+1]):
            numbers_coordinates.append([x+1, y])
    # up neighbour
    if y > 0:
        if is_number(grid[y-1][x]):
            has_up_mid = True
            numbers_coordinates.append([x, y-1])
    # down neighbour
    if y < len(grid)-1:
        if is_number(grid[y+1][x]):
            has_down_mid = True
            numbers_coordinates.append([x, y+1])
        
    # diagonals
    # up left neighbour
    if x > 0 and y > 0:
        if is_number(grid[y-1][x-1]) and not has_up_mid:
            numbers_coordinates.append([x-1, y-1])
    # up right neighbour
    if x < len(grid[0])-1 and y > 0:
        if is_number(grid[y-1][x+1]) and not has_up_mid:
            numbers_coordinates.append([x+1, y-1])
    # down left neighbour
    if x > 0 and y < len(grid)-1:
        if is_number(grid[y+1][x-1]) and not has_down_mid:
            numbers_coordinates.append([x-1, y+1])
    # down right neighbour
    if x < len(grid[0])-1 and y < len(grid)-1:
        if is_number(grid[y+1][x+1]) and not has_down_mid:
            numbers_coordinates.append([x+1, y+1])
    
    # clean up any connecting numbers in the candidates
    number_of_numbers = len(numbers_coordinates)
    if number_of_numbers < 2:
        return False
    if number_of_numbers > 2:
        return False
    
    numbers = []

    # Here we have two coordinates which are part of a number. We play it back to the left and then get the number.
    for coordinate in numbers_coordinates:
        x = coordinate[0]
        y = coordinate[1]

        start_x, start_y = playback_number(grid, x, y)

        numbers.append(int(get_number(grid, start_x, start_y)))
    return numbers


def run(part=1, file='test'):
    text_file = open(f"./day3/{file}.txt")
    lines = text_file.readlines()

    grid = []

    for line in lines:
        line = line.strip('\n')
        row = []
        for char in line:
            row.append(char)
        grid.append(row)

    answer = 0

    y = 0
    while y < len(grid):
        x = 0
        while x < len(grid[0]):
            if part == 1:
                number = get_number(grid, x, y)

                if number is None:
                    x += 1
                    continue
                value_length = len(str(number or '.'))
                number_has_surrounding_symbols = has_surrounding_symbols(grid, x, y, value_length)
                if number_has_surrounding_symbols:
                    answer += int(number)
                x += value_length
            elif part == 2:
                # if the char at grid x,y is a *, we need to check if it is a gear.
                # it is a gear if it connects to two seperate numbers.
                # if it is a gear, we multiply the two numbers and add it to the answer.
                if grid[y][x] != '*':
                    x += 1
                    continue

                numbers = has_two_surrounding_numbers_and_returns(grid, x, y)
                
                if numbers:
                    [number1, number2] = numbers
                    print(f"Found gear at {x},{y} with numbers {number1} and {number2}")

                    # print 5 by 5 grid around x and y
                    #for y2 in range(y-1, y+2):
                    #    for x2 in range(x-4, x+4):
                    #        print(grid[y2][x2], end='')    
                    #    print()
                    #print('done', number1 * number2)

                    answer += number1 * number2
                x += 1          
        y += 1
        
    print(answer)
    text_file.close()

run(2, 'input')