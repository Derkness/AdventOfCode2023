options = ['#','.']

def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append(strippedLine)
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
    
if __name__ == "__main__":
    part_1()