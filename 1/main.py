FIND_REPLACE_NUMBERS = [
    ["one", "1"],
    ["two", "2"],
    ["three", "3"],
    ["four", "4"],
    ["five", "5"],
    ["six", "6"],
    ["seven", "7"],
    ["eight", "8"],
    ["nine", "9"],
]

def part_1():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            line = line[:-1]
            lines.append([int(char) for char in line if char.isdigit()])
    return lines

def part_2():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            line = replaceWordNumber(line[:-1])
            lines.append([int(char) for char in line if char.isdigit()])
    return lines

def replaceWordNumber(line):
    for pair in FIND_REPLACE_NUMBERS:
        line = line.replace(pair[0], pair[0]+pair[1]+pair[0])
    return line
    

if __name__ == "__main__":
    totalValue = 0
    lines = part_2()
    for line in lines:
        totalValue += line[0]*10+line[-1]
    print(totalValue)