import re


class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        
    def total(self):
        return self.x + self.m + self.a + self.s


def get_input():
    workflows=[]
    parts=[]
    
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                if (strippedLine[0] == '{'):
                    parts.append(strippedLine)
                    continue
                workflows.append(strippedLine)
    return (workflows, parts)

def generate_map(workflows):
    map = {}
    for workflow in workflows:
        key, value = re.split('\{|\}', workflow)[0:2]
        rules = value.split(',')
        map[key]=rules
    return map

def process_part(workflowMap, part):
    state="in"
    while state != 'R' and state != 'A':
        state = get_new_state(workflowMap[state], part)
    return part.total() if state == 'A' else 0
        
def get_new_state(rules, part):
    for rule in rules:
        if "<" in rule:
            attribute, value, destination =  re.split('<|:', rule)
            if getattr(part, attribute) < int(value):
                return destination
            continue
        if ">" in rule:
            attribute, value, destination =  re.split('>|:', rule)
            if getattr(part, attribute) > int(value):
                return destination
            continue
        return rule

def part_1():
    workflows, parts = get_input()
    workflowMap = generate_map(workflows)
    count = 0
    for part in parts:
        x, m, a, s = [partLine[2::] for partLine in part[1:-1].split(',')]
        count += process_part(workflowMap, Part(int(x),int(m),int(a),int(s)))
    print(count)
    
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __str__(self):
        return str(self.start) + " - " + str(self.end)
    
    def width(self):
        return self.end - self.start + 1

class Group:
    def __init__(self, x1, x2, m1, m2, a1, a2, s1, s2, state = 'in'):
        self.x = Range(x1, x2)
        self.m = Range(m1, m2)
        self.a = Range(a1, a2)
        self.s = Range(s1, s2)
        self.state = state
        
    def full():
        return Group(1, 4000, 1, 4000, 1, 4000, 1, 4000)
    
    def from_group(group):
        return Group(group.x.start, group.x.end, group.m.start, group.m.end, group.a.start, group.a.end, group.s.start, group.s.end, group.state)
    
    def __str__(self):
        return "state: " + self.state + "| x: " + str(self.x) + ", m: " + str(self.m) + ", a: " + str(self.a) + ", s: " + str(self.s)
    
    def __repr__(self):
        return str(self)

def non_terminated(groups: set[Group]):
    for group in groups:
        if group.state not in ['A', 'R']:
            return True
    return False

def split_groups(state, rules, groups: set[Group]):
    newGroups = set()
    for group in groups:
        if (group.state != state):
            newGroups.add(group)
            continue
        for rule in rules:
            if "<" in rule:
                attribute, value, destination =  re.split('<|:', rule)
                if getattr(group, attribute).end < int(value):
                    newGroup = Group.from_group(group)
                    newGroup.state = destination
                    newGroups.add(newGroup)
                    break
                
                elif getattr(group, attribute).start < int(value) - 1:
                    newGroup = Group.from_group(group)
                    getattr(newGroup, attribute).end = int(value) - 1
                    newGroup.state = destination
                    newGroups.add(newGroup)
                    getattr(group, attribute).start = int(value)
                continue
            
            
            if ">" in rule:
                attribute, value, destination =  re.split('>|:', rule)
                if getattr(group, attribute).start > int(value):
                    newGroup = Group.from_group(group)
                    newGroup.state = destination
                    newGroups.add(newGroup)
                    break
                elif getattr(group, attribute).end > int(value) + 1:
                    newGroup = Group.from_group(group)
                    getattr(newGroup, attribute).start = int(value) + 1
                    newGroup.state = destination
                    newGroups.add(newGroup)
                    getattr(group, attribute).end = int(value)
                continue
            
            
            group.state = rule
            newGroups.add(group)
    return newGroups
    

def part_2():
    workflows, _ = get_input()
    workflowMap = generate_map(workflows)
    groups = {Group.full()}
    while non_terminated(groups):
        for key, value in workflowMap.items():
            groups = split_groups(key, value, groups)
    count = 0
    for group in groups:
        if group.state == 'A':
            count += group.x.width() * group.m.width() * group.a.width() * group.s.width()
    print(count)

if __name__ == "__main__":
    part_2()
    167409079868000
    1430940609190821640000
    167010937327821