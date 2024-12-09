def read_input(input_file_dir):
    lines = open(input_file_dir, 'r')
    lines = [line.strip() for line in lines]
    return lines


# Part 1
def scan_messages(messages, target):
    word_cnt = len(target)
    occurrences = 0
    # scan row
    for y in range(len(messages)):
        # scan column
        for x in range(len(messages[y])):
            if x + word_cnt <= len(messages[y]):
                horizontal = messages[y][x:x+word_cnt]
                if horizontal == target or horizontal == target[::-1]:
                    occurrences += 1
            if y + word_cnt <= len(messages):
                vertical = ''.join(messages[y+k][x] for k in range(word_cnt))
                if vertical == target or vertical == target[::-1]:
                    occurrences += 1
            if x + word_cnt <= len(messages[y]) and y + word_cnt <= len(messages):
                diagonal = ''.join(messages[y+k][x+k] for k in range(word_cnt))
                if diagonal == target or diagonal == target[::-1]:
                    occurrences += 1
                reversed_diagonal = ''.join(messages[y+word_cnt-k-1][x+k] for k in range(word_cnt))
                if reversed_diagonal == target or reversed_diagonal == target[::-1]:
                    occurrences += 1
    return occurrences


# Part 2
def scan_messages_v2(messages, target):
    word_cnt = len(target)
    occurrences = 0
    for y in range(len(messages)):
        for x in range(len(messages[y])):
            diagonal_flag = False
            reversed_diagonal_flag = False
            # check only diagonal and reverse diagonal
            if x + word_cnt <= len(messages[y]) and y + word_cnt <= len(messages):
                diagonal = ''.join(messages[y+k][x+k] for k in range(word_cnt))
                if diagonal == target or diagonal == target[::-1]:
                    diagonal_flag = True
                reversed_diagonal = ''.join(messages[y+word_cnt-k-1][x+k] for k in range(word_cnt))
                if reversed_diagonal == target or reversed_diagonal == target[::-1]:
                    reversed_diagonal_flag = True
                if diagonal_flag and reversed_diagonal_flag:
                    occurrences += 1
    return occurrences

messages_input = read_input('./input.txt')
print(scan_messages_v2(messages_input, 'MAS'))

