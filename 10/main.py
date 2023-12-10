x_bound = None
y_bound = None

class Coordinate: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def get_up(self):
        if self.x > 0:
            return Coordinate(self.x-1, self.y)
        
    def get_left(self):
        if self.y > 0:
            return Coordinate(self.x, self.y-1)
        
    def get_down(self):
        if self.x < x_bound:
            return Coordinate(self.x+1, self.y)
        
    def get_right(self):
        if self.y < y_bound:
            return Coordinate(self.x, self.y+1)
        
    def __str__(self):
        return "X: " + str(self.x) + ", Y: " + str(self.y)

class Link:
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

connecting_map = {
    '|': Link(['|', '7', 'F', 'S'], ['|', 'J','L', 'S'], [], []), 
    '-': Link([], [], ['-', 'L', 'F', 'S'], ['-', 'J','7', 'S']), 
    'L': Link(['|', '7', 'F', 'S'], [], [], ['7', '-', 'J', 'S']),
    'J': Link(['|', '7', 'F', 'S'], [], ['L', '-', 'F', 'S'], []),
    '7': Link([], ['|', 'J','L', 'S'], ['L', '-', 'F', 'S'], []),
    'F': Link([], ['|', 'J','L', 'S'], [], ['7', '-', 'J', 'S']),
    'S': Link(['|', '7', 'F', 'S'], ['|', 'J','L', 'S'], ['L', '-', 'F', 'S'], ['7', '-', 'J', 'S']),
    '.':[],
}

def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append([x for x in strippedLine])
    global x_bound
    x_bound = len(lines) - 1
    global y_bound
    y_bound = len(lines[0]) - 1
    return lines

def connects(previousPipe, newPipe, direction):
    if (previousPipe == '.' or newPipe == '.'):
        return False

    return newPipe in getattr(connecting_map[previousPipe], direction)

def get_options(lines, location: Coordinate, previous: Coordinate):
    options = []
    
    if location.get_up() is not None and connects(get_value(lines, location), get_value(lines, location.get_up()), 'up'):
        options.append(location.get_up())
        
    if location.get_left() is not None and connects(get_value(lines, location), get_value(lines, location.get_left()), 'left'):
        options.append(location.get_left())
        
    if location.get_right() is not None and connects(get_value(lines, location), get_value(lines, location.get_right()), 'right'):
        options.append(location.get_right())
        
    if location.get_down() is not None and connects(get_value(lines, location), get_value(lines, location.get_down()), 'down'):
        options.append(location.get_down())
        
    return [x for x in options if (previous == None or str(x) != str(previous))]

def get_value(lines, location: Coordinate):
    return lines[location.x][location.y]
    

def part_1():
    lines = get_input()
    location = None
    previousLocation = None
    for x, line in enumerate(lines):
        if 'S' in line:
            location = Coordinate(x, line.index("S"))
            break
    options = get_options(lines, location, previousLocation)
    previousLocation = location
    location = options[0]
    count = 0
    while get_value(lines, location) != 'S':
        options = get_options(lines, location, previousLocation)
        previousLocation = location
        location = options[0]
        count+=1

    print(int(count/2)+1) # +1 bc of int rounding just chops off decimal
    
def part_2():
    lines = get_input()
    location = None
    previousLocation = None
    for x, line in enumerate(lines):
        if 'S' in line:
            location = Coordinate(x, line.index("S"))
            break
    all_locations = [location]
    options = get_options(lines, location, previousLocation)
    previousLocation = location
    location = options[0]
    all_locations.append(location)
    count = 0
    while get_value(lines, location) != 'S':
        options = get_options(lines, location, previousLocation)
        previousLocation = location
        location = options[0]
        all_locations.append(location)

    string_all_letters = [str(x) for x in all_locations]

    for x, line in enumerate(lines):
        inside = False
        for y, pipe in enumerate(line):
            if (str(Coordinate(x, y)) in string_all_letters):
                if pipe in  ['|', 'L', 'J',]:
                    inside = not inside
                continue
            if (inside):
                count+=1
    print(count)
        
    
if __name__ == "__main__":
    part_2()
    # Part 1:
    # Too low: 456
    # just right: 7066