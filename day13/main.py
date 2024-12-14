def read_input(input_file_dir):
    lines = open(input_file_dir, 'r')
    arcades = []
    arcade = {}
    for line in lines:
        line = line.strip()
        if line == '':
            arcade = {}
        if line.startswith('Button A:'):
            line = line.replace('Button A: X+', '')
            line = line.replace(' Y+', '')
            units = line.split(',')
            arcade['A'] = (int(units[0]), int(units[1]))
        if line.startswith('Button B:'):
            line = line.replace('Button B: X+', '')
            line = line.replace(' Y+', '')
            units = line.split(',')
            arcade['B'] = (int(units[0]), int(units[1]))
        if line.startswith('Prize:'):
            line = line.replace('Prize: X=', '')
            line = line.replace(' Y=', '')
            units = line.split(',')
            arcade['Prize'] = (int(units[0]), int(units[1]))
            arcades.append(arcade)
    return arcades

def calculate_token(arcades):
    tokens = 0
    for arcade in arcades:
        ax, ay = arcade['A']
        bx, by = arcade['B']
        px, py = arcade['Prize']

        b = ((px * ay) - (py * ax)) / ((bx * ay) - (by * ax))

        if b < 0 or not b.is_integer():
            continue

        a = (px - bx * b) / ax

        if a < 0 or not a.is_integer():
            continue

        tokens += 3 * a + 1 * b

    return int(tokens)


arcades_input = read_input('./input.txt')
print(calculate_token(arcades_input))