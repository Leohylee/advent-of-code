def read_input(input_file_dir):
    with open(input_file_dir, 'r') as file:
        stones_line = file.readline().strip().split(' ')
        stone_dict = {}
        for stone in stones_line:
            if stone not in stone_dict:
                stone_dict[stone] = 1
            else:
                stone_dict[stone] += 1
    return stone_dict


def blink(stones_dict):
    new_dict = {}
    for stone, occurrence in stones_dict.items():
        stones = []
        if stone == '0':
            stones.append('1')
        elif len(stone) % 2 == 0:
            half = len(stone) // 2
            stones.append(stone[0:half])
            stones.append(str(int(stone[half:])))
        else:
            stones.append(str(int(stone) * 2024))
        for new_stone in stones:
            if new_stone not in new_dict:
                new_dict[new_stone] = occurrence
            else:
                new_dict[new_stone] += occurrence
    return new_dict


def calculate_stones(stones, times):
    for _ in range(times):
        stones = blink(stones)
    total = 0
    for occurrence in stones.values():
        total += occurrence
    return total


stones_input = read_input('./input.txt')
print(calculate_stones(stones_input, 75))


# Part 1 -> Part 2: Using dict instead of list
