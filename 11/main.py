from typing import List


class Coordinate: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def manhattan_distance_from(self, other):
        return abs(self.x-other.x) + abs(self.y-other.y)

growthRate = None

def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append([x for x in strippedLine])
    return lines

def expand(lines):
    expanded = []
    for line in lines:
        if '#' not in line:
            expanded.append(line.copy())
        expanded.append(line.copy())

    noGalaxies = list(range(len(expanded[0])))
    for line in expanded:
        for index, value in enumerate(line):
            if value == '#':
                noGalaxies[index] = "Tombstone"
    noGalaxies = [x for x in noGalaxies if (x != "Tombstone")]
    noGalaxies.reverse()
    for line in expanded:
        for location in noGalaxies:
            line.insert(location, '.')
    return expanded

def part_1():
    lines = get_input()
    expandedLines = expand(lines)
    galaxies: List[Coordinate] = []
    for x, line in enumerate(expandedLines):
        for y, value in enumerate(line):
            if value == '#':
                galaxies.append(Coordinate(x,y))
    count = 0
    for main, galaxy in enumerate(galaxies):
        for otherGalaxyIndex in range(main + 1, len(galaxies)):
            count += galaxy.manhattan_distance_from(galaxies[otherGalaxyIndex])
    print(count)    

def mark_as_expanded(lines):
    expanded = []
    for line in lines:
        if '#' not in line:
            expanded.append(['+'] * len(line))
            continue
        expanded.append(line.copy())

    noGalaxies = list(range(len(expanded[0])))
    for line in expanded:
        for index, value in enumerate(line):
            if value == '#':
                noGalaxies[index] = "Tombstone"
    noGalaxies = [x for x in noGalaxies if (x != "Tombstone")]
    noGalaxies.reverse()
    for line in expanded:
        for location in noGalaxies:
            line[location] = '+'
    return expanded

def get_effective_distance(char):
    if char == '+':
        return growthRate
    return 1

def distance(galaxy, otherGalaxy, lines):
    totalDistance = 0
    xDistance = galaxy.x-otherGalaxy.x
    yDistance = galaxy.y-otherGalaxy.y
    while xDistance != 0:
        totalDistance += get_effective_distance(lines[otherGalaxy.x + xDistance][otherGalaxy.y + yDistance])
        if xDistance > 0:
            xDistance -= 1
        elif xDistance < 0:
            xDistance += 1
    while yDistance != 0:
        totalDistance += get_effective_distance(lines[otherGalaxy.x + xDistance][otherGalaxy.y + yDistance])
        if yDistance > 0:
            yDistance -= 1
        elif yDistance < 0:
            yDistance += 1
    return totalDistance

def part_2():
    global growthRate
    growthRate = int(input("What's the growth rate of the empty space? "))
    lines = get_input()
    expandedLines = mark_as_expanded(lines)
    galaxies: List[Coordinate] = []
    for x, line in enumerate(expandedLines):
        for y, value in enumerate(line):
            if value == '#':
                galaxies.append(Coordinate(x,y))
    count = 0
    for main, galaxy in enumerate(galaxies):
        for otherGalaxyIndex in range(main + 1, len(galaxies)):
            count += distance(galaxy, galaxies[otherGalaxyIndex], expandedLines)
    print(count)

if __name__ == "__main__":
    part_2()