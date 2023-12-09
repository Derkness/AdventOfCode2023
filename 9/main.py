def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append([int(x) for x in strippedLine.split()])
    return lines

def find_pattern(line):
    return [line[i+1] - line[i] for i in range(len(line) - 1)]

def extrapolate_value(line):
    nest = [line]
    while not (len(set(nest[-1])) == 1 and 0 in nest[-1]):
        nest.append(find_pattern(nest[-1]))
    nest.reverse()
    increment = None
    for level in nest:
        if (increment is not None):
            level.append(level[-1] + increment)
        increment = level[-1]
        # print(increment)
    return nest[-1].pop()
        
def part_1():
    lines = get_input()
    count = 0
    for line in lines:
        count += extrapolate_value(line)
    print(count)


def extrapolate_previous_value(line):
    nest = [line]
    while not (len(set(nest[-1])) == 1 and 0 in nest[-1]):
        nest.append(find_pattern(nest[-1]))
    nest.reverse()
    increment = None
    for level in nest:
        if (increment is not None):
            level.insert(0, level[0] - increment)
        increment = level[0]
    return nest[-1][0]
        
def part_2():
    lines = get_input()
    count = 0
    for line in lines:
        count += extrapolate_previous_value(line)
    print(count)

if __name__ == "__main__":
    part_2()