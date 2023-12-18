class Point:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2
        
    def right(self, amount = 1):
        return Point(self.dim1, self.dim2 + amount)

    def left(self, amount = 1):
        return Point(self.dim1, self.dim2 - amount)

    def up(self, amount = 1):
        return Point(self.dim1 - amount, self.dim2)

    def down(self, amount = 1):
        return Point(self.dim1 + amount, self.dim2)
        
    def replace_right(self):
        self.dim2 += 1

    def replace_left(self):
        self.dim2 -= 1

    def replace_up(self):
        self.dim1 -= 1

    def replace_down(self):
        self.dim1 += 1
    
    def __str__(self):
        return "(" + str(self.dim1) + ", " + str(self.dim2) + ")"
    
    def __repr__(self):
        return str(self)


def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append(strippedLine)
    return lines

def normalise_points(points: list[Point]): # Turns out I didn't need this. I thought I'd generate the grid and count the '#'. SO FOOLISH
    normalised = False
    while not normalised:
        normalised = True
        moveRight = False
        moveDown = True
        for point in points:
            if (point.dim1 < 0):
                moveDown = True
                normalised = False
            if (point.dim2 < 0):
                moveRight = True
                normalised = False
        for point in points:
            if moveRight:
                point.replace_right()
            if moveDown:
                point.replace_down()
    return points

def get_area(points: list[Point]): # Also don't need this, just use the trapezoid shoestring thing
    maxDim1 = 0
    maxDim2 = 0
    
    for point in points:
        maxDim1 = max(maxDim1, point.dim1)
        maxDim2 = max(maxDim2, point.dim2)
    
    grid = [["." for _ in range(maxDim2 + 1)] for _ in range(maxDim1 + 1)]
    
    for point in points:
        grid[point.dim1][point.dim2] = '#'
    
    for lineIndex, line in enumerate(grid):
        seenSoFar = False
        total = line.count("#")
        for charIndex, char in enumerate(line):
            if char == '#':
                seenSoFar += 1
                continue
            if (seenSoFar + total) % 2 == 1:
                grid[lineIndex][charIndex] = '#'
                
    [print(x) for x in grid]
    
    count = 0
    for line in grid:
        count += line.count("#")
    
    return count

def get_area_trapezoid(points: list[Point]):
    area = 0
    for i in range(1, len(points)):
        one = points[i - 1]
        two = points[i]
        area += (one.dim2 + two.dim2) * (one.dim1 - two.dim1)

    area = (abs(area) + len(points) + 1) / 2
    return area

def get_area_trapezoid_2(points: list[Point], mCovered):
    area = 0
    for i in range(1, len(points)):
        one = points[i - 1]
        two = points[i]
        area += (one.dim2 + two.dim2) * (one.dim1 - two.dim1)

    area = (abs(area) + mCovered + 1) / 2
    return area
            

def part_1():
    lines = [[a[0], int(a[1])] for a in [x.split()[0:2] for x in get_input()]]
    points = [Point(0, 0)]
    for line in lines:
        match line[0]:
            case 'R':
                while line[1] > 0:
                    points.append(points[-1].right())
                    line[1] -= 1
            case 'L':
                while line[1] > 0:
                    points.append(points[-1].left())
                    line[1] -= 1
            case 'U':
                while line[1] > 0:
                    points.append(points[-1].up())
                    line[1] -= 1
            case 'D':
                while line[1] > 0:
                    points.append(points[-1].down())
                    line[1] -= 1
    print(get_area_trapezoid(points))
    
def process_line(line):
    options = ['R', 'D', 'L', 'U']
    distance = line[2:7]
    return " ".join([options[int(line[7])], str(int(distance, 16))])
    
def part_2():
    lines = [y[2] for y in [x.split() for x in get_input()]]
    lines = [[a[0], int(a[1])] for a in [process_line(line).split() for line in lines]]
    corners = [Point(0, 0)]
    totalMetresCovered = 1
    for line in lines:
        totalMetresCovered += line[1]
        match line[0]:
            case 'R':
                corners.append(corners[-1].right(line[1]))
            case 'L':
                corners.append(corners[-1].left(line[1]))
            case 'U':
                corners.append(corners[-1].up(line[1]))
            case 'D':
                corners.append(corners[-1].down(line[1]))
    print(get_area_trapezoid_2(corners, totalMetresCovered))

    
if __name__ == "__main__":
    part_2()