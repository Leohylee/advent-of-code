def read_input(input_file_dir):
    lines = open(input_file_dir, 'r')
    lines = [list(line.strip()) for line in lines]
    return lines

def patrol(guard_map, x, y, move):
    try:
        if move == 'up':
            y -= 1
            if guard_map[y][x] == '#':
                move = 'right'
                y += 1
        elif move == 'down':
            y += 1
            if guard_map[y][x] == '#':
                move = 'left'
                y -= 1
        elif move == 'left':
            x -= 1
            if guard_map[y][x] == '#':
                move = 'up'
                x += 1
        elif move == 'right':
            x += 1
            if guard_map[y][x] == '#':
                move = 'down'
                x -= 1
        guard_map[y][x] = 'X'
    except IndexError:
        print("The guard has left.")
    return guard_map, x, y, move

def find_guard(guard_map, height, width):
    moves = {'^': 'up', 'v': 'down', '<': 'left', '>': 'right'}
    for j in range(height):
        for i in range(width):
            if guard_map[j][i] in moves:
                move = moves.get(guard_map[j][i])
                guard_map[j][i] = 'X'
                return move, i, j

def count_move(guard_map):
    if len(guard_map) <= 0:
        return
    height = len(guard_map)
    width = len(guard_map[0])
    move, x, y = find_guard(guard_map, height, width)
    if move != '':
        while 0 < x < width and 0 < y < height:
            guard_map, x, y, move = patrol(guard_map, x, y, move)
        cnt = 0
        for j in range(height):
            for i in range(width):
                if guard_map[j][i] == 'X':
                    cnt += 1
        return cnt

lines_input = read_input('./input.txt')
print(count_move(lines_input))

# ^<>v