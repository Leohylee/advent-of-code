def read_input(input_file_dir):
    with open(input_file_dir, 'r') as file:
        lines = file.readlines()
    reports = []
    for line in lines:
        line = line.split(' ')
        reports.append(line)
    return reports

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
def count_safe(reports):
    cnt = 0
    for report in reports:
        if is_safe(report): cnt += 1
    return cnt

# Part 2
def count_safe_with_dampener(reports):
    cnt = 0
    for report in reports:
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

if __name__ == "__main__":
    reports = read_input('./input.txt')
    print(count_safe_with_dampener(reports))

