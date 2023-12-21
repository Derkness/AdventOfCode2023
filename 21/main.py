GARDEN = '.'
ROCK = '#'
START = 'S'
VISITED = 'X'

class Point:
    def __init__(self, dim1, dim2, visitedOn):
        self.dim1 = dim1
        self.dim2 = dim2
        self.visitedOn = visitedOn
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.dim1 == other.dim1) and (self.dim2 == other.dim2) and (self.visitedOn == other.visitedOn)
        return False
    
    def __hash__(self):
        return hash((self.dim1, self.dim2, self.visitedOn))
        
    def right(self, step):
        return Point(self.dim1, self.dim2 + 1, step)

    def left(self, step):
        return Point(self.dim1, self.dim2 - 1, step)

    def up(self, step):
        return Point(self.dim1 - 1, self.dim2, step)

    def down(self, step):
        return Point(self.dim1 + 1, self.dim2, step)
    
    def __str__(self):
        return "(" + str(self.dim1) + ", " + str(self.dim2) + ") - Visited on: " + str(self.visitedOn)
    
    def __repr__(self):
        return str(self)

def get_input():
    lines=[]
    point = None
    with open("input.txt", "r") as file:
        for dim1, line in enumerate(file):
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append([x for x in strippedLine])
                if START in line:
                    point = Point(dim1, [x for x in strippedLine].index(START), 0)
    return lines, point

def validate_point_in_range(lines, possibility: Point):
    if possibility.dim1 < 0:
        return False
    if possibility.dim1 >= len(lines):
        return False
    if possibility.dim2 < 0:
        return False
    if possibility.dim2 >= len(lines[0]):
        return False
    if lines[possibility.dim1][possibility.dim2] == ROCK:
        return False
    return True

def spread(lines, current: set[Point], steps) -> set[Point]:
    for e in current:
        break
    result = {e}
    nextCurrent = set()
    for step in range(1, steps+1):
        
        for possibility in current:
            adjacents = {possibility.left(step%2), possibility.right(step%2), possibility.up(step%2), possibility.down(step%2)}
            adjacents = {x for x in adjacents if validate_point_in_range_2(lines, x)}
            nextCurrent.update(adjacents)
            result.update(adjacents)
        
        current = nextCurrent
        nextCurrent = set()
    return result

def validate_point_in_range_2(lines, possibility: Point):
    if lines[possibility.dim1 % len(lines)][possibility.dim2 % len(lines[0])] == ROCK:
        return False
    return True

def wrap_points_around(lines, point: Point) -> Point:
    return Point(point.dim1 % len(lines), point.dim2 % len(lines[0]), point.visitedOn)

def spread_2(lines, current: set[Point], steps) -> set[Point]:
    for e in current:
        break
    result = {e}
    nextCurrent = set()
    for step in range(1, steps+1):
        print(step, len(current))

        for possibility in current:
            adjacents = {possibility.left(step%2), possibility.right(step%2), possibility.up(step%2), possibility.down(step%2)}
            # wrappedAdjacents = {wrap_points_around(lines, x) for x in adjacents}
            # validAdjacents = {x for x in wrappedAdjacents if validate_point_in_range_2(lines, x)}
            validAdjacents = {x for x in adjacents if validate_point_in_range_2(lines, x)}
            nextCurrent.update(validAdjacents)
            result.update(validAdjacents)
        
        current = nextCurrent
        nextCurrent = set()
    return result
            
        

def part_1():
    lines, sPoint = get_input()
    possibles = {sPoint}
    points = spread(lines, possibles, 64)
    count = 0
    for point in points:
        if point.visitedOn == 0:
            count += 1
    print(count)
    
# def part_2():
#     lines, sPoint = get_input()
#     possibles = {sPoint}
#     points = spread_2(lines, possibles, 330)
#     count = 0
#     for point in points:
#         if point.visitedOn == 0:
#             count += 1
#     print(count)

def part_2():
    [3882, 34441, 95442]
    # just use online quad calc lol
    # logic being that the step count is kinda weird, and it quickly becomes 202300 lots of 131, which is the input length
    # also if u map the initial to a quadratic it SORT of is a quadratic, they just didn't use 131 as the difference in steps
    # so find the first 3, and then theres a way u can work out a quadratic using an online calculator
    # idk why im writing this. I'm just so happy it worked lol
    
    
if __name__ == "__main__":
    part_2()

# 64+indexOffset 3882
# 64+131+indexOffset 34441
# 64+262+indexOffset 95442

# using online calculator, gives us 15221x^2 + 15338x + 3882
# feeding in 2023 gives 62323416565, which is too low (because it's actually 202300 and I didn't see OMG)
# 202300 gives 622926941971282
