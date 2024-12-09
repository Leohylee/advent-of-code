def read_input(input_file_dir):
    with open(input_file_dir, 'r') as file:
        lines = file.readlines()
    output = []
    for line in lines:
        line = line.split(' ')
        output.append(line)
    return output

def is_safe(report):
    if len(report) < 2:
        return True
    prev = int(report[0])
    is_increasing = int(report[1]) - prev > 0
    for level in report[1:]:
        curr = int(level)
        difference = curr - prev
        if abs(difference) == 0 or abs(difference) > 3 or (not (difference > 0) == is_increasing):
            return False
        prev = curr
    return True

# Part 1
def count_safe(reports_input):
    cnt = 0
    for report in reports_input:
        if is_safe(report): cnt += 1
    return cnt

# Part 2
def count_safe_with_dampener(reports_input):
    cnt = 0
    for report in reports_input:
        if is_safe(report):
            cnt += 1
        else:
            for idx in range(len(report)):
                cpy = report.copy()
                cpy.pop(idx)
                if is_safe(cpy):
                    cnt += 1
                    break
    return cnt

reports = read_input('./input.txt')
print(count_safe_with_dampener(reports))

