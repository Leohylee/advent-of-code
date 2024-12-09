import math

def read_input(input_file_dir):
    with open(input_file_dir, 'r') as file:
        lines = file.readlines()
    list_left = []
    list_right = []
    for line in lines:
        line = line.encode('ascii', 'ignore').strip()
        location = line.split()
        list_left.append(int(location[0]))
        list_right.append(int(location[1]))
    return list_left, list_right

# Part 1
def calculate_distance(list_left, list_right):
    total_distance = 0
    list_left.sort()
    list_right.sort()
    for i in range(len(list_left)):
        total_distance += (math.fabs(list_left[i] - list_right[i]))
    return total_distance

# Part 2
def calculate_similarity_score(list_left, list_right):
    occurrence = {}
    score = 0
    for number in list_left:
        if number not in occurrence:
            occurrence[number] = 1
        else:
            occurrence[number] += 1
    for number in list_right:
        if number in occurrence:
            score += number * occurrence[number]
    return score

left, right = read_input('./input.txt')
print(calculate_similarity_score(left, right))


