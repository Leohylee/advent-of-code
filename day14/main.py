from math import floor


def read_input(input_file_dir):
    lines = open(input_file_dir, 'r')
    robots = []
    count = 0
    for line in lines:
        count += 1
        line = line.strip().replace('p=', '').replace('v=', '').replace(' ', ',')
        robots.append(tuple(line.split(',')))
    return robots, count

def robots_move(robots, time):
    robots_position = {}
    for px, py, vx, vy in robots:
        px, py, vx, vy = int(px), int(py), int(vx), int(vy)
        x = (px + vx * time) % width
        y = (py + vy * time) % height
        if (x,y) not in robots_position:
            robots_position[(x,y)] = 1
        else:
            robots_position[(x,y)] += 1
    # for part 2
    print('Second: ', time)
    grid = []
    for j in range(height):
        row = []
        for i in range(width):
            row.append('.')
        grid.append(row)
    for x, y in robots_position:
        grid[y][x] = '#'
    for row in grid:
        print(''.join(row))
    return robots_position

def quadrants_count(positions, time):
    tl, tr, bl, br = 0, 0, 0, 0
    mid = (floor(width/2), floor(height/2))
    for position, count in positions.items():
        # top left quadrant
        if position[0] < mid[0] and position[1] < mid[1]:
            tl += count
        # top right quadrant
        if position[0] > mid[0] and position[1] < mid[1]:
            tr += count
        # bottom left quadrant
        if position[0] < mid[0] and position[1] > mid[1]:
            bl += count
        # bottom right quadrant
        if position[0] > mid[0] and position[1] > mid[1]:
            br += count
    # for part 2
    portion = total_robots * 0.50
    if tl >= portion or tr >= portion or bl >= portion or br >= portion:
        return time

robots_input, total_robots = read_input('input.txt')
times = 10000
width = 101
height = 103
robots_move(robots_input, 6771)
# for second in range(times):
#     result = quadrants_count(robots_move(robots_input, second), second)
#     if result is not None:
#         print(result)
# print(quadrants_count(robots_move(robots_input)))