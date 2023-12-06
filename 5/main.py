global_dict = {}

def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append(strippedLine)
    return lines

def is_map_heading(line):
    return "map" in line

def key_from_heading(line):
    [name, _] = line.split(" ")
    return name

# Map format is:
# {start, end, adjustment}
def build_map(lines):
    dict = {}
    dictKey = ""
    for line in lines:
        if (is_map_heading(line)):
            dictKey = key_from_heading(line)
            continue
        [destinationStart, sourceStart, length] = [int(x) for x in line.split(" ")]
        existingValue = dict.get(dictKey, [])
        existingValue.append({'start': sourceStart, 'end': sourceStart + length - 1, 'adjustment': destinationStart - sourceStart})
        dict[dictKey] = existingValue
    return dict

def get_location_from_seed(value, sourceMaterial):
    key = get_required_key(sourceMaterial)
    if (key is None):
        return value
    
    newValue = get_adjusted_value(global_dict[key], value)
    
    target = key.split("-")[2]
    return get_location_from_seed(newValue, target)
            
    
def get_required_key(sourceMaterial):
    keys = [x for x in global_dict.keys()]
    for index, key in enumerate([x.split("-") for x in global_dict.keys()]):
        if key[0] == sourceMaterial:
            return keys[index]
    return None



# Map format is:
# {start, end, adjustment}
def get_adjusted_value(conversions, value):
    for conversion in conversions:
        if (conversion['start'] <= value <= conversion['end']):
            return value + conversion['adjustment']
    return value
        

def part_1():
    global global_dict
    lines = get_input()
    [_, seeds] = [x.split() for x in lines.pop(0).split(":")]
    global_dict = build_map(lines)
    locations = []
    for seed in seeds:
        locations.append(get_location_from_seed(int(seed), "seed"))
    closest = min(locations)
    print(closest)
    
def condense(seedPairs):
    if not seedPairs:
        return []

    newRanges = [seedPairs[0]]  # Start with the first range

    for i in range(1, len(seedPairs)):
        currentPair = seedPairs[i]
        lastNewRange = newRanges[-1]

        # Check if the current pair overlaps with the last added range
        mergedRange = new_range(lastNewRange, currentPair)

        if mergedRange:
            # If they overlap, replace the last range in newRanges
            newRanges[-1] = mergedRange
        else:
            # If they don't overlap, add the current pair to newRanges
            newRanges.append(currentPair)

    return newRanges
        
def new_range(pair1, pair2):
    if pair1[1] >= pair2[0]:
        return (min(pair1[0], pair2[0]), max(pair1[1], pair2[1]))
    return None
        

def part_2():
    global global_dict
    lines = get_input()
    [_, seeds] = [x.split() for x in lines.pop(0).split(":")]
    seedPairs = [tuple(seeds[i:i + 2]) for i in range(0, len(seeds), 2)]
    seedPairs = [(int(x), int(x)+int(y)) for [x, y] in seedPairs]
    seedPairs.sort(key=lambda x: x[0])
    print(seedPairs)
    print('--')
    condensedPairs = seedPairs
    previousLength = 0
    while len(condensedPairs) != previousLength:
        previousLength = len(condensedPairs)
        condensedPairs = condense(condensedPairs)
        condensedPairs.sort(key=lambda x: x[0])
    # expandedSeeds = [num for x, y in condensedPairs for num in range(int(x), int(y))]
    for pair in condensedPairs:
        expandedSeeds = range(pair[0], pair[1])
        global_dict = build_map(lines)
        locations = []
        for seed in expandedSeeds:
            locations.append(get_location_from_seed(int(seed), "seed"))
        closest = min(locations)
        print(closest)
    

if __name__ == "__main__":
    part_2()