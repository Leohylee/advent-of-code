import math

def read_input(input_file_dir):
    with open(input_file_dir, 'r') as file:
        lines = file.readlines()
    left = []
    right = []
    for line in lines:
        line = line.encode('ascii', 'ignore').strip()
        location = line.split()
        left.append(int(location[0]))
        right.append(int(location[1]))
    return left, right

def calculate_distance(left, right):
    total_distance = 0
    left.sort()
    right.sort()
    for i in range(len(left)):
        total_distance += (math.fabs(left[i] - right[i]))
    return total_distance

def calculate_similarity_score(left, right):
    occurance = {}
    score = 0
    for number in left:
        if number not in occurance:
            occurance[number] = 1
        else:
            occurance[number] += 1
    for number in right:
        if number in occurance:
            score += number * occurance[number]
    return score

if __name__ == "__main__":
    left, right = read_input('./input.txt')
    print(calculate_similarity_score(left, right))


