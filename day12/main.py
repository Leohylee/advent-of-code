from collections import deque

def read_input(input_file_dir):
    lines = open(input_file_dir, 'r')
    grid = [list(line.strip()) for line in lines]
    return grid

def get_regions(grid):
    rows = len(grid)
    cols = len(grid[0])
    regions = []
    seen = set()
    for y in range(rows):
        for x in range(cols):
            if (x, y) in seen: continue
            seen.add((x, y))
            region = {(x,y)}
            q = deque([(x, y)])
            plant = grid[y][x]
            while q:
                i, j = q.popleft()
                for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if ni < 0 or ni >= cols or nj < 0 or nj >= rows: continue
                    if grid[nj][ni] != plant: continue
                    if (ni, nj) in region: continue
                    region.add((ni, nj))
                    q.append((ni, nj))
            seen |= region
            regions.append(region)
    return regions

# Part 1
def calculate_cost(regions):
    cost = 0
    for region in regions:
        perimeter = 0
        for (x, y) in region:
            perimeter += 4
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if (nx, ny) in region: perimeter -= 1
        cost += perimeter * len(region)
    return cost

# Part 2
def calculate_cost_v2(regions):
    cost = 0
    for region in regions:
        perimeter = 0
        for (x, y) in region:
            perimeter += 4
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if (nx, ny) in region: perimeter -= 1
        cost += perimeter * len(region)
    return cost

grid_input = read_input('./input.txt')
print(calculate_cost(get_regions(grid_input)))