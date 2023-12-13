import re
from functools import cache
from itertools import product

# biggest possible chain is '???????????????'
RULE_MAP = {
    '1': [''.join(x) for x in (product('.?', repeat=1))],
    '2': [''.join(x) for x in (product('.?', repeat=2))],
    '3': [''.join(x) for x in (product('.?', repeat=3))],
    '4': [''.join(x) for x in (product('.?', repeat=4))],
    '5': [''.join(x) for x in (product('.?', repeat=5))],
    '6': [''.join(x) for x in (product('.?', repeat=6))],
    '7': [''.join(x) for x in (product('.?', repeat=7))],
    '8': [''.join(x) for x in (product('.?', repeat=8))],
    '9': [''.join(x) for x in (product('.?', repeat=9))],
    '10': [''.join(x) for x in (product('.?', repeat=10))],
    '11': [''.join(x) for x in (product('.?', repeat=11))],
    '12': [''.join(x) for x in (product('.?', repeat=12))],
    '13': [''.join(x) for x in (product('.?', repeat=13))],
    '14': [''.join(x) for x in (product('.?', repeat=14))],
    '15': [''.join(x) for x in (product('.?', repeat=15))]
}
# RULE_MAP = {str(i): [''.join(x) for x in product('.?', repeat=i)] for i in range(1, 76)}

print('prepped map')


def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append(strippedLine)
    return lines

def get_input_2():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                [springs, rules] = strippedLine.split()
                newSprings = '?'.join([springs]*5) + '.' # Add an extra dot at the end so that all clusters will 'end'
                newRules = tuple([int(x) for x in rules.split(',')]) * 5
                lines.append([newSprings, newRules])
    return lines

# def is_valid(line): <-------- Maybe use this for tree pruning if part 2 calls for it
#     [springs, rules] = line.split(" ")
#     groups = [x for x in springs.split(".") if x != '']
#     ruleList = [int(x) for x in rules.split(",")]
#     if len(groups) > len(ruleList):
#         return False
#     springGroups = [x for x in springs.replace('?','.').split(".") if x != '']
    
#     print(line)
    
#     if '?' not in line:
#         for index, group in enumerate(springGroups):
#             # if index >= len(ruleList):
#             #     print('escaped at: ' + str(index))
#             #     break
#             if len(group) >= ruleList[index]:
#                 return False
#     print(line)
#     print(groups)
#     print(ruleList)
#     print('------')
#     return True

# Assumes the line is complete
def is_valid(line):
    [springs, rules] = line.split(" ")
    groups = [x for x in springs.split(".") if x != '']
    ruleList = [int(x) for x in rules.split(",")]
    if len(groups) != len(ruleList):
        return False
    for i in range(len(groups)):
        if len(groups[i]) != ruleList[i]:
            return False
    return True

def get_combinations(line):
    
    if '?' not in line:
        if is_valid(line):
            return 1
        else:
            return 0
    else:
        withBroken = line.replace('?','.', 1)
        withWorking = line.replace('?','#', 1)
        return get_combinations(withBroken) + get_combinations(withWorking)
    

def part_1():
    lines = get_input()
    count = 0
    for line in lines:
        count += get_combinations(line)
    print(count)
    
# def is_valid(line): <-------- Maybe use this for tree pruning if part 2 calls for it
#     [springs, rules] = line.split(" ")
#     groups = [x for x in springs.split(".") if x != '']
#     ruleList = [int(x) for x in rules.split(",")]
#     if len(groups) > len(ruleList):
#         return False
#     springGroups = [x for x in springs.replace('?','.').split(".") if x != '']
    
#     print(line)
    
#     if '?' not in line:
#         for index, group in enumerate(springGroups):
#             # if index >= len(ruleList):
#             #     print('escaped at: ' + str(index))
#             #     break
#             if len(group) >= ruleList[index]:
#                 return False
#     print(line)
#     print(groups)
#     print(ruleList)
#     print('------')
#     return True

# biggest possible chain is '???????????????'
def get_possible_rules(springs):
     # Split the input string into placeholder and non-placeholder parts
    parts = re.split(r'(\?+)', springs)

    # For each part, if it's a placeholder, get the corresponding value from RULE_MAP
    parts = [RULE_MAP[str(len(part))] if part.startswith('?') else [part] for part in parts]

    # Generate all combinations
    return [''.join(combination) for combination in product(*parts)]

    # e.g.
    # ..#.#.#?????.#.#
    # could be
    # [1, 1, 1, 1, 1]
    # [1, 1, 2, 1, 1]
    # [1, 1, 1, 1, 1]
    # [1, 1, 1, 1, 1]
    # [1, 1, 1, 1, 1]
    # [1, 1, 1, 1, 1]
    
def is_impossible(line):
    [springs, rules] = line.split(" ")
    possibleRules = get_possible_rules(springs)
    # groups = [x for x in springs.replace("?",'.').split(".") if x != '']
    ruleList = [int(x) for x in rules.split(",")]
    return ruleList in possibleRules
    
    # for index, group in enumerate(groups):
    #     if index >= len(ruleList):
    #         break
    #     if len(group) > ruleList[index]:
    #         return True
    
    # return False
@cache
def get_combinations_2(springs, rules, lengthOfCurrentGroup):
    if len(springs) == 0:
        if len(rules) == 0 and lengthOfCurrentGroup == 0:
            return 1
        return 0
    count = 0
    waveform = ['.', '#'] if springs[0] == '?' else springs[0]
    for collapse in waveform:
        if collapse == '#': # continue the current group
            count += get_combinations_2(springs[1:], rules, lengthOfCurrentGroup + 1)
        else:
            if lengthOfCurrentGroup != 0: # . End the current group
                if rules and rules[0] == lengthOfCurrentGroup:
                    count += get_combinations_2(springs[1:], rules[1:], 0)
            else:  # Just move on. Still not in a group, but nothing changes here
                count += get_combinations_2(springs[1:], rules, 0)
    return count
    # if is_impossible(line):
        # return 0
    # withBroken = line.replace('?','.', 1)
    # withWorking = line.replace('?','#', 1)
    # return get_combinations_2(withBroken) + get_combinations_2(withWorking)
    
def part_2():
    lines = get_input_2()
    count = 0
    for line in lines:
        [springs, rules] = line
        count += get_combinations_2(springs, rules, 0)
    print(count)
    
if __name__ == "__main__":
    part_2()