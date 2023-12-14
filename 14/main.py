from functools import cmp_to_key


def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append([x for x in strippedLine])
    return lines

def gravity(line):
    start = 0
    rocks = 0
    for index, char in enumerate(line):
        if char == "O":
            rocks += 1
            continue
        if char == '#':
            spaces = index - start - rocks
            line[start:start+spaces] = ['.'] * (spaces)
            line[(start+spaces):(start+spaces) + rocks] = ['O'] * (rocks)
            start = index + 1
            rocks = 0
    spaces = len(line) - start - rocks
    line[start:start+spaces] = ['.'] * (spaces)
    line[(start+spaces):(start+spaces) + rocks] = ['O'] * (rocks)
    return line

def tilt_north(lines):
    lines=[[y for y in x] for x in zip(*lines)]
    for index, line in enumerate(lines):
        line.reverse()
        lines[index] = gravity(line)
        line.reverse()
    lines=[[y for y in x] for x in zip(*lines)]
    return lines

def tilt_south(lines):
    lines=[[y for y in x] for x in zip(*lines)]
    for index, line in enumerate(lines):
        lines[index] = gravity(line)
    lines=[[y for y in x] for x in zip(*lines)]
    return lines

def tilt_west(lines):
    for index, line in enumerate(lines):
        line.reverse()
        lines[index] = gravity(line)
        line.reverse()
    return lines

def tilt_east(lines):
    for index, line in enumerate(lines):
        lines[index] = gravity(line)
    return lines
    
def get_score(lines):
    score = 0
    lines.reverse()
    for index, line in enumerate(lines):
        score += line.count('O') * (index+1)
    lines.reverse()
    return score
    
    

def part_1():
    lines =  tilt_north(get_input())
    score = get_score(lines)
    print(score)
    
def part_2():
    lines = get_input()
    previousLines = []
    for i in range(1000000000):
        # [print(x) for x in lines]
        # print('--------------')
        # if i % 10000 == 0:
            # print(i/1000000000)
            # [print(x) for x in lines]
            # print('---------------------')
        previousLines.append(lines.copy())
        # [print(x) for x in lines]
        # print('-----------------')
        lines = tilt_north(lines)
        # [print(x) for x in lines]
        # print('-----------------')
        lines = tilt_west(lines)
        # [print(x) for x in lines]
        # print('-----------------')
        lines = tilt_south(lines)
        # [print(x) for x in lines] 
        # print('-----------------')
        lines = tilt_east(lines)
        # [print(x) for x in lines]
        # print('-----------------')
        if lines in previousLines:
            # [print(x) for x in lines]
            # print('------------')
            # [print(x) for x in previousLines[previousLines.index(lines)]]
            loopLength = i - previousLines.index(lines)
            while (i+loopLength) % 1000000 != 8:
                lines = tilt_north(lines)
                lines = tilt_west(lines)
                lines = tilt_south(lines)
                lines = tilt_east(lines)
                loopLength -= 1
            break
    score = get_score(lines)
    print(score)
    
    
if __name__ == "__main__":
    part_2()
    
# Part 1
# Too low:
# 105314

# Just right = 113424

# Part 2:
# Too high:
# 96020
# 96014
# Too Low:
# 95981
# 95971
# 95962
# 95961

# WRONG
# 95985
# 96001

# TO Try:
# 96003 <-------- try next IT WORKED