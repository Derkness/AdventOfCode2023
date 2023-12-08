from math import lcm


def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append(strippedLine.replace("(","").replace(")",""))
    return lines

def build_map(lines):
    map = {}
    for line in lines:
        [key, paths] = line.split(" = ")
        [left, right] = paths.split(", ")
        map[key] = {'L': left, 'R': right}
    return map

def part_1():
    lines = get_input()
    steps = lines.pop(0)
    map = build_map(lines)
    currentPlace = "AAA"
    count = 0
    length = len(steps)
    while 1 == 1:
        currentPlace = map[currentPlace][steps[count%length]]
        count +=1
        if (currentPlace == "ZZZ"):
            break
    print(count)
    
def all_finished(currentPlaces):
    for place in currentPlaces:
        if place[2] != 'Z':
            return False
    return True

def part_2():
    lines = get_input()
    steps = lines.pop(0)
    map = build_map(lines)
    currentPlaces = [x for x in map.keys() if x[2] == "A"]
    loopLengths = [0]*len(currentPlaces)
    count = 0
    length = len(steps)
    while 1 == 1:
        currentPlaces = [map[x][steps[count%length]] for x in currentPlaces]
        for i in range(len(currentPlaces)):
            if currentPlaces[i][2] == "Z" and loopLengths[i] == 0:
                loopLengths[i] = count + 1
                break
        count +=1
        if (0 not in loopLengths):
            break
    print(lcm(*loopLengths))
    
    
    
if __name__ == "__main__":
    part_2()