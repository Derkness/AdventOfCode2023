BROADCASTER=1
FLIPFLOP=2
CONJUNCTION=3

LOW=0
HIGH=1

strengths = ["LOW", "HIGH"]
types = ["_", "BROADCASTER", "FLIPFLOP", "CONJUNCTION"]

def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append(strippedLine)
    return lines

class Signal:
    def __init__(self, source, destination, strength):
        self.source = source
        self.destination = destination
        self.strength = strength
        
    def __str__(self):
        return str(self.source) + " -> " + str(self.destination) + ", Strength: " + strengths[self.strength]
        
    def __repr__(self):
        return str(self)

class Node:
    def __init__(self, type, id, links):
        self.type = int(type)
        self.id = id
        self.links = links
        self.state = False
        self.memory = {}
    
    def __str__(self):
        return "Type: " + types[self.type] + ", id: " + str(self.id) + ", links: " + str(self.links) 
    
    def __repr__(self):
        return str(self)
        
    def parse_line(line):
        if '%' in line:
            id, linkString = line[1:].split(' -> ')
            return Node(FLIPFLOP, id, linkString.split(', '))
        
        if '&' in line:
            id, linkString = line[1:].split(' -> ')
            return Node(CONJUNCTION, id, linkString.split(', '))
                    
        id, linkString = line.split(' -> ')
        return Node(BROADCASTER, id, linkString.split(', '))
    
    def recieve_signal(self, signal: Signal):
        if self.type == FLIPFLOP:
            if signal.strength == LOW:
                self.state = not self.state
                if self.state:
                    return [Signal(self.id, id, HIGH) for id in self.links]
                return [Signal(self.id, id, LOW) for id in self.links]
            return []
        elif self.type == CONJUNCTION:
            self.memory[signal.source] = signal.strength
            
            allHigh = True
            
            for memory in self.memory.values():
                if memory == LOW:
                    allHigh = False
                    break
            if allHigh:
                return [Signal(self.id, id, LOW) for id in self.links]
            return [Signal(self.id, id, HIGH) for id in self.links]
        elif self.type == BROADCASTER:
            return [Signal(self.id, id, signal.strength) for id in self.links]
        
    def add_to_memory(self, id):
        self.memory[id] = LOW
            
            
                
    
def part_1():
    lines = get_input()
    nodes = [Node.parse_line(x) for x in lines]
    for node in nodes:
        if node.type != CONJUNCTION:
            continue
        pointingToNode = []
        for otherNode in nodes:
            if node.id in otherNode.links:
                pointingToNode.append(otherNode.id)
        for pointerNode in pointingToNode:
            node.add_to_memory(pointerNode)
    highCount = 0
    lowCount = 0
    for _ in range(1000):
        signals = [Signal('', 'broadcaster', LOW)]
        while len(signals) != 0:
            signal = signals.pop(0)
            # print(signal)
            destinationNode = next((x for x in nodes if x.id == signal.destination), None)
            if destinationNode is not None:
                signals.extend(destinationNode.recieve_signal(signal))
            if signal.strength == LOW:
                lowCount += 1
            elif signal.strength == HIGH:
                highCount += 1
                
    print(highCount, lowCount, highCount * lowCount)
            
            
                
    
def part_1():
    lines = get_input()
    nodes = [Node.parse_line(x) for x in lines]
    for node in nodes:
        if node.type != CONJUNCTION:
            continue
        pointingToNode = []
        for otherNode in nodes:
            if node.id in otherNode.links:
                pointingToNode.append(otherNode.id)
        for pointerNode in pointingToNode:
            node.add_to_memory(pointerNode)
    notDelivered = True
    presses = 0
    while notDelivered:
        presses += 1
        signals = [Signal('', 'broadcaster', LOW)]
        while len(signals) != 0:
            signal = signals.pop(0)
            if signal.destination == 'rx' and signal.strength == LOW:
                notDelivered = False
                print(signal.destination)
            destinationNode = next((x for x in nodes if x.id == signal.destination), None)
            if destinationNode is not None:
                signals.extend(destinationNode.recieve_signal(signal))
                
    print(presses)
    
if __name__ == "__main__":
    part_1()