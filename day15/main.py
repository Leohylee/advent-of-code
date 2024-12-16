def read_input(input_file_dir):
    lines = open(input_file_dir, 'r')
    grid = []
    moves = []
    robot = (0,0)
    split_flag = False
    for y, line in enumerate(lines):
        line = line.strip()
        if line == '':
            split_flag = True
        if not split_flag:
            row = []
            for x, node in enumerate(line):
                row.append(node)
                if node == '@':
                    robot = (x, y)
            grid.append(row)
        else:
            for move in line:
                moves.append(move)
        y += 1
    return grid, moves, robot

def attempt_move(grid, old, new, item):
    wall = False
    if grid[new[1]][new[0]] == '#':
        return grid, old, True
    elif grid[new[1]][new[0]] == '.':
        grid[new[1]][new[0]] = item
    elif grid[new[1]][new[0]] == 'O':
        x_diff = new[0] - old[0]
        y_diff = new[1] - old[1]
        grid, new, wall = attempt_move(grid, new, (new[0] + x_diff, new[1] + y_diff), 'O')
        if not wall:
            grid[new[1]][new[0]] = item
    if not wall:
        grid[old[1]][old[0]] = '.'
    if item == 'O' or wall:
        curr = old
    else:
        curr = new
    return grid, curr, wall

def robot_perform_moves(grid, moves, robot):
    i = 1
    for move in moves:
        print('Move ', i, ': ', move)
        if move == '<':
            grid, robot, _ = attempt_move(grid, robot, (robot[0] - 1, robot[1]), '@')
        elif move == '>':
            grid, robot, _ = attempt_move(grid, robot, (robot[0] + 1, robot[1]), '@')
        elif move == '^':
            grid, robot, _ = attempt_move(grid, robot, (robot[0], robot[1] - 1), '@')
        elif move == 'v':
            grid, robot, _ = attempt_move(grid, robot, (robot[0], robot[1] + 1), '@')
        for row in grid:
            print(row)
        i += 1
    return grid

def calculate_coordinates(grid):
    coordinates = 0
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if item == 'O':
                coordinates += 100 * y + x
    return coordinates

grid_input, moves_input, robot_input = read_input('input.txt')
grid = robot_perform_moves(grid_input, moves_input, robot_input)
print(calculate_coordinates(grid))
