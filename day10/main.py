def read_input(input_file_dir):
    lines = open(input_file_dir, 'r')
    map = []
    for line in lines:
        map_row = []
        for location in line.strip():
            map_row.append(int(location))
        map.append(map_row)
    return map


def draft_trail(map, x, y, map_width, map_height, current_height, goal, cnt):
    if current_height == 9:
        goal.add((x, y))
        cnt += 1
        return goal, cnt
    # left
    if x - 1 >= 0 and map[y][x - 1] == current_height + 1:
        updated_goal, updated_cnt = draft_trail(map, x - 1, y, map_width, map_height, map[y][x - 1], goal, cnt)
        goal = goal | updated_goal
        cnt = updated_cnt
    # right
    if x + 1 < map_width and map[y][x + 1] == current_height + 1:
        updated_goal, updated_cnt = draft_trail(map, x + 1, y, map_width, map_height, map[y][x + 1], goal, cnt)
        goal = goal | updated_goal
        cnt = updated_cnt
    # up
    if y - 1 >= 0 and map[y - 1][x] == current_height + 1:
        updated_goal, updated_cnt = draft_trail(map, x, y - 1, map_width, map_height, map[y - 1][x], goal, cnt)
        goal = goal | updated_goal
        cnt = updated_cnt
    # down
    if y + 1 < map_height and map[y + 1][x] == current_height + 1:
        updated_goal, updated_cnt = draft_trail(map, x, y + 1, map_width, map_height, map[y + 1][x], goal, cnt)
        goal = goal | updated_goal
        cnt = updated_cnt
    return goal, cnt


def calculate_map_scores(map):
    scores = 0
    ratings = 0
    map_width = len(map[0])
    map_height = len(map)
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                goals, rating = draft_trail(map, x, y, map_width, map_height, 0, set(), 0)
                scores += len(goals)
                ratings += rating
    return scores, ratings


map_input = read_input('./input.txt')
print(calculate_map_scores(map_input))
