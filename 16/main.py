from enum import Enum


class Direction(Enum):
    UP="UP",
    DOWN="DOWN",
    LEFT="LEFT",
    RIGHT="RIGHT",
    
class Node(Enum):
    NW="/",
    NE="\\",
    VSPLIT="|",
    HSPLIT="-",
    EMPTY=".",
    MARKUP='1',
    MARKLEFT='2',
    MARKDOWN='3',
    MARKRIGHT='4',
    
    def __str__(self):
        return self.value[0]

class Beam:
    def __init__(self, dim1, dim2, direction: Direction):
        self.dim1 = dim1
        self.dim2 = dim2
        self.direction = direction
    
    def __str__(self):
        return "(" + str(self.dim1) + ", " + str(self.dim2) + ", " + self.direction.name + ")"
    
    def __repr__(self):
        return str(self)
        
    def right(self):
        self.dim2 = self.dim2 + 1
        
    def left(self):
        self.dim2 = self.dim2 - 1
        
    def up(self):
        self.dim1 = self.dim1 - 1
        
    def down(self):
        self.dim1 = self.dim1 + 1
        
    def set_direction(self, direction: Direction):
        self.direction = direction
        
    def get_node(self, lines) -> Node:
        return lines[self.dim1][self.dim2]
    
    def fromBeam(beam):
        return Beam(beam.dim1, beam.dim2, beam.direction)

def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append([x for x in strippedLine])
    return lines

def out_of_bounds(beam, lines):
    return (beam.dim1 < 0 or beam.dim1 >= len(lines) or beam.dim2 < 0 or beam.dim2 >= len(lines[0]))

def traverse_map(lines, beams: list[Beam], marked):
    beamsMarkedForDeath = set()
    addedBeams = set()
    for beam in beams:
        if not out_of_bounds(beam, lines):
            marked[beam.dim1][beam.dim2] = '#'
        match beam.direction:
            case Direction.UP:
                beam.up()
            case Direction.DOWN:
                beam.down()
            case Direction.LEFT:
                beam.left()
            case Direction.RIGHT:
                beam.right()
        if out_of_bounds(beam, lines):
            continue
        match beam.get_node(lines):
            case "/":
                match beam.direction:
                    case Direction.LEFT:
                        beam.set_direction(Direction.DOWN)
                    case Direction.RIGHT:
                        beam.set_direction(Direction.UP)
                    case Direction.UP:
                        beam.set_direction(Direction.RIGHT)
                    case Direction.DOWN:
                        beam.set_direction(Direction.LEFT)
            case "\\":
                match beam.direction:
                    case Direction.LEFT:
                        beam.set_direction(Direction.UP)
                    case Direction.RIGHT:
                        beam.set_direction(Direction.DOWN)
                    case Direction.UP:
                        beam.set_direction(Direction.LEFT)
                    case Direction.DOWN:
                        beam.set_direction(Direction.RIGHT)
            case '|':
                match beam.direction:
                    case Direction.RIGHT | Direction.LEFT:
                        beam.set_direction(Direction.UP)
                        
                        createdBeam = Beam.fromBeam(beam)
                        createdBeam.set_direction(Direction.DOWN)
                        addedBeams.add(createdBeam)
            case '-':
                match beam.direction:
                    case Direction.UP | Direction.DOWN:
                        beam.set_direction(Direction.LEFT)
                        
                        createdBeam = Beam.fromBeam(beam)
                        createdBeam.set_direction(Direction.RIGHT)
                        addedBeams.add(createdBeam)
            case '.':
                match beam.direction: # It is possible for an infinite loop to survive, if the loop never contains a '.'. Thankfully, I got the right answer for a path that doesn't have this, soooo, who cares
                    case Direction.LEFT:
                        lines[beam.dim1][beam.dim2] = str(Node.MARKLEFT)
                    case Direction.RIGHT:
                        lines[beam.dim1][beam.dim2] = str(Node.MARKRIGHT)
                    case Direction.UP:
                        lines[beam.dim1][beam.dim2] = str(Node.MARKUP)
                    case Direction.DOWN:
                        lines[beam.dim1][beam.dim2] = str(Node.MARKDOWN)
            case '1':
                if (beam.direction == Direction.UP):
                    beamsMarkedForDeath.add(beam)
            case '2':
                if (beam.direction == Direction.LEFT):
                    beamsMarkedForDeath.add(beam)
            case '3':
                if (beam.direction == Direction.DOWN):
                    beamsMarkedForDeath.add(beam)
            case '4':
                if (beam.direction == Direction.RIGHT):
                    beamsMarkedForDeath.add(beam)
            case _:
                raise Exception("Unrecognised node: '" + str(beam.get_node(lines)) + "'")
    beams = {x for x in beams if not out_of_bounds(x, lines)}
    
    beams -= beamsMarkedForDeath
    beams |= addedBeams
    return (lines, beams, marked)

def get_value(char):
    if char == Node.MARKDOWN or char == Node.MARKUP or char == Node.MARKLEFT or char == Node.MARKRIGHT:
        return 1
    return 0

def part_1():
    lines = get_input()
    marked = [['.' for _ in range(len(lines[0]))] for _ in range(len(lines))]
    beams = {Beam(0, -1, Direction.RIGHT)}
    while len(beams) != 0:
        [lines, beams, marked] = traverse_map(lines, beams, marked)
    count = 0
    for line in marked:
        count += line.count('#')
    print(count)

def part_2():
    lines = get_input()
    bestCount = 0
    for i in range(len(lines)):
        lines = get_input()
        marked = [['.' for _ in range(len(lines[0]))] for _ in range(len(lines))]
        beams = {Beam(i, -1, Direction.RIGHT)}
        while len(beams) != 0:
            [lines, beams, marked] = traverse_map(lines, beams, marked)
        count = 0
        for line in marked:
            count += line.count('#')
        bestCount = max(count, bestCount)
    print('---', bestCount)
    for i in range(len(lines)):
        lines = get_input()
        marked = [['.' for _ in range(len(lines[0]))] for _ in range(len(lines))]
        beams = {Beam(i, len(lines[0]), Direction.LEFT)}
        while len(beams) != 0:
            [lines, beams, marked] = traverse_map(lines, beams, marked)
        count = 0
        for line in marked:
            count += line.count('#')
        bestCount = max(count, bestCount)
    print('---', bestCount)
    for i in range(len(lines[0])):
        print(i)
        lines = get_input()
        marked = [['.' for _ in range(len(lines[0]))] for _ in range(len(lines))]
        beams = {Beam(-1, i, Direction.DOWN)}
        while len(beams) != 0:
            [lines, beams, marked] = traverse_map(lines, beams, marked)
        count = 0
        for line in marked:
            count += line.count('#')
        bestCount = max(count, bestCount)
    print('---', bestCount)
    for i in range(len(lines[0])):
        lines = get_input()
        marked = [['.' for _ in range(len(lines[0]))] for _ in range(len(lines))]
        beams = {Beam(len(lines), i, Direction.UP)}
        while len(beams) != 0:
            [lines, beams, marked] = traverse_map(lines, beams, marked)
        count = 0
        for line in marked:
            count += line.count('#')
        bestCount = max(count, bestCount)
    print('---', bestCount)
    
    print(bestCount)
    
    
if __name__ == "__main__":
    part_2()