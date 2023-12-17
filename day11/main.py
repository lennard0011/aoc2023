
def run(part=1, file='test'):
    with open(f'day11/{file}.txt') as f:
        lines = f.readlines()

    # Initiate the grid
    grid = []
    for line in lines:
        grid.append(list(line.replace('\n', '')))

    double_distance_rows = []

    for index, row in enumerate(grid):
        if all([char != '#' for char in row]):
            double_distance_rows.append(index)
    
    double_distance_columns = []

    for column_index in range(len(grid[0])):
        if all([row[column_index] != '#' for row in grid]):
            double_distance_columns.append(column_index)

    galaxies = []
    for row_index, row in enumerate(grid):
        for column_index, char in enumerate(row):
            if char == '#':
                galaxies.append([row_index, column_index])

    distances = []

    galaxy_pairs = [(galaxy_i, galaxy_j) for idx, galaxy_i in enumerate(galaxies) for galaxy_j in galaxies[idx + 1:]]

    empty_line_width = 1 if part == 1 else (1_000_000 - 1)

    for galaxy_i, galaxy_j in galaxy_pairs:
        pair_distance = abs(galaxy_i[0] - galaxy_j[0]) + abs(galaxy_i[1] - galaxy_j[1])
        
        min_row = min(galaxy_i[0], galaxy_j[0])
        max_row = max(galaxy_i[0], galaxy_j[0])
        min_column = min(galaxy_i[1], galaxy_j[1])
        max_column = max(galaxy_i[1], galaxy_j[1])

        for row_index in double_distance_rows:
            if min_row < row_index < max_row:
                pair_distance += empty_line_width
        for column_index in double_distance_columns:
            if min_column < column_index < max_column:
                pair_distance += empty_line_width

        distances.append(pair_distance)

    print(sum(distances))           

# 82000210 too low
# 82000292 too low
# 82000374 too low
    
# standard answer is 292. But we got 82 overlaps. 
run(2, 'input')