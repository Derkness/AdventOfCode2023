def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append(strippedLine)
    return "".join(lines).split(',')

def get_hash(lump):
    count = 0
    for char in lump:
        count += ord(char)
        count = (count * 17) % 256
    return count

def part_1():
    lumps = get_input()
    count = 0
    for lump in lumps:
        count += get_hash(lump)
    print(count)
    
def part_2():
    lumps = get_input()
    map = {}
    for lump in lumps:
        if '-' in lump:
            label = lump.split('-')[0]
            hash = get_hash(label)
            if hash in map.keys():
                map[hash] = [x for x in map[hash] if x[0] != label]
                if map[hash] == []:
                    del map[hash]
        else:
            [label, foculLength] = lump.split("=")
            hash = get_hash(label)
            newLabel = (label, foculLength)
            box = map.get(hash, [])
            if label not in [x[0] for x in box]:
                box.append(newLabel)
                map[hash] = box
                continue
            index = [x[0] for x in box].index(label)
            box[index] = newLabel
            map[hash] = box
    count = 0
    
    for [id, box] in map.items():
        for lensId, lens in enumerate(box):
            count += (1 + id) * (lensId + 1) * int(lens[1])
    print(count)
   

if __name__ == "__main__":
   part_2()