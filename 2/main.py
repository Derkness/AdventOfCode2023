def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    return lines

def get_val(value, colour):
    return int(value.replace(" " + colour, ""))

def part_1():
    numRed = int(input("How many red? "))
    numGreen = int(input("How many green? "))
    numBlue = int(input("How many blue? "))
    
    colourPairs = [
        ["red", numRed],
        ["green", numGreen],
        ["blue", numBlue],
    ]
    
    count = 0
    lines = get_input()
    for line in lines:
        [gameName, gameContents] = line.split(':')
        gameId = int(gameName.replace("Game ",""))
        
        gameStages = [x.strip() for x in gameContents.split(';')]
        possible = True
        for gameStage in gameStages:
            colours = [x.strip() for x in gameStage.split(',')]
            for colour in colours:
                for colourPair in colourPairs:
                    if colourPair[0] in colour:
                        if colourPair[1] < get_val(colour, colourPair[0]):
                            possible = False
                            break
                if possible == False:
                    break
            if possible == False:
                break
        if (possible):
            count += gameId            
    print(count)

def part_2():
    count = 0
    lines = get_input()
    for line in lines:
        [_, gameContents] = line.split(':')
        
        colourMaximums = [
            ["red", 0],
            ["green", 0],
            ["blue", 0],
        ]
        
        gameStages = [x.strip() for x in gameContents.split(';')]
        for gameStage in gameStages:
            colours = [x.strip() for x in gameStage.split(',')]
            for colour in colours:
                for colourMaximum in colourMaximums:
                    if colourMaximum[0] in colour:
                        colourMaximum[1] = max(colourMaximum[1], get_val(colour, colourMaximum[0]))

        power = 1
        for colourMaximum in colourMaximums:
            power *= colourMaximum[1]
            
        count += power

    print(count)
    
if __name__ == "__main__":
    part_2()