def read_input(input_file_dir):
    lines = open(input_file_dir, 'r')
    lines = [line.strip().split(':') for line in lines]
    targets = []
    values = []
    for line in lines:
        targets.append(line[0])
        values.append(line[1].strip().split(' '))
    return targets, values

def scan_values(target, values, current):
    if len(values) == 0 and target == current:
        return True
    if len(values) == 0 and target != current:
        return False
    operators = ['add', 'multiply', 'combine']
    for operator in operators:
        if operator == 'add':
            update = current + values[0]
            is_target = scan_values(target, values[1:], update)
            if is_target:
                return is_target
        if operator == 'multiply':
            update = current * values[0]
            is_target = scan_values(target, values[1:], update)
            if is_target:
                return is_target
        if operator == 'combine':
            update = int(str(current) + str(values[0]))
            is_target = scan_values(target, values[1:], update)
            if is_target:
                return is_target
    return False

def get_total_calibration(targets_list, values_list):
    cnt = 0
    for i in range(len(targets_list)):
        if len(values_list[i]) > 1:
            values = [int(value) for value in values_list[i]]
            if scan_values(int(targets_list[i]), values[1:], values[0]):
                cnt += int(targets_list[i])
    return cnt

if __name__ == "__main__":
    targets_input, values_input = read_input('./input.txt')
    print(get_total_calibration(targets_input, values_input))