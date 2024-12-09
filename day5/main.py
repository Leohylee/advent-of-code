def read_input(input_file_dir):
    lines = open(input_file_dir, 'r')
    lines = [line.strip() for line in lines]
    rules = []
    updates = []
    for i in range(len(lines)):
        if len(lines[i]) == 0:
            rules = lines[:i]
            updates = lines[i+1:]
    return rules, updates


def process_rules(rules):
    rules_dict = {}
    for rule in rules:
        rule = rule.split('|')
        if rule[1] not in rules_dict:
            rules_dict[rule[1]] = {rule[0]}
        else:
            rules_dict[rule[1]].add(rule[0])
    return rules_dict


def is_correctly_order(rules, update):
    for i, page in enumerate(update):
        if rules.get(page) is not None and not rules.get(page).isdisjoint(set(update[i+1:])):
            return False
    return True

# Part 1
def calculate_total(rules, updates):
    sum = 0
    for update in updates:
        update = update.split(',')
        if is_correctly_order(rules, update):
            mid = (len(update) - 1)/2
            sum += int(update[int(mid)])
    return sum

# Part 2
def reorder_update(rules, update):
    for i, page in enumerate(update):
        rest = update[i + 1:]
        if rules.get(page) is not None and not rules.get(page).isdisjoint(set(rest)):
            intersects = rules.get(page).intersection(rest)
            index = 0
            for intersect in intersects:
                if rest.index(intersect) > index:
                    index = rest.index(intersect)
            rest.insert(index+1, page)
            return update[:i] + reorder_update(rules, rest)
    return update


def calculate_total_after_correction(rules, updates):
    sum = 0
    for update in updates:
        update = update.split(',')
        if not is_correctly_order(rules, update):
            update = reorder_update(rules, update)
            mid = (len(update) - 1) / 2
            sum += int(update[int(mid)])
    return sum

rules_input, updates_input = read_input('./input.txt')
print(calculate_total_after_correction(process_rules(rules_input), updates_input))

