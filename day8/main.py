def read_input(input_file_dir):
    lines = open(input_file_dir, 'r')
    lines = [list(line.strip()) for line in lines]
    _antenna_map = {}
    for y, line in enumerate(lines):
        for x, location in enumerate(line):
            if location == '.':
                continue
            if location not in _antenna_map:
                _antenna_map[location] = [[x,y]]
            else:
                _antenna_map[location].append([x,y])
    return lines, _antenna_map

def populate_antinode(raw_map, antenna_map):
    antinodes = set()
    height = len(raw_map)
    width = len(raw_map[0])
    for coordinates in antenna_map.items():
        for coordinate in coordinates[1]:
            for coordinate_alt in coordinates[1]:
                difference = [coordinate[0] - coordinate_alt[0], coordinate[1] - coordinate_alt[1]]
                if difference[0] != 0 or difference[1] != 0:
                    # Part 2
                    antinode = [coordinate[0], coordinate[1]]
                    while 0 <= antinode[0] < width and 0 <= antinode[1] < height:
                        antinodes.add((antinode[0], antinode[1]))
                        antinode = [antinode[0] + difference[0], antinode[1] + difference[1]]
    sorted(antinodes)
    return len(antinodes)

if __name__ == "__main__":
    map_input, antenna_map_input = read_input('./input.txt')
    print(populate_antinode(map_input, antenna_map_input))


# antenna_map = {antenna: {[x, y]...}...}
# map[x,y] = "./A/a/..."
# map_width
# map_height

# for line in lines:
    # for location in line:
        # location -> (x,y) -> antenna_map[location] = (x,y)
# cnt = 0
# for antenna in antenna_map:
    # for coordinate in antenna:
        # for coordinate_alt in antenna:
            # difference = coordinate - coordinate_alt
            # antinode = coordinate + difference
            # if difference > 0 and 0 <= antinodeX < width and 0 <= antinodeY < height + map[antinodeX, antinodeY] == '.':
                # map[antinodeX, antinodeY] = '#'
                # cnt += 1
