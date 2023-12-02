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
                if "red" in colour:
                    if numRed < get_val(colour, "red"):
                        possible = False
                        break
                if "blue" in colour:
                    if numBlue < get_val(colour, "blue"):
                        possible = False
                        break
                if "green" in colour:
                    if numGreen < get_val(colour, "green"):
                        possible = False
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
        [gameName, gameContents] = line.split(':')
        gameId = int(gameName.replace("Game ",""))
        
        maxRed = 0
        maxGreen = 0
        maxBlue = 0
        
        gameStages = [x.strip() for x in gameContents.split(';')]
        for gameStage in gameStages:
            colours = [x.strip() for x in gameStage.split(',')]
            for colour in colours:
                if "red" in colour:
                    maxRed = max(maxRed, get_val(colour, "red"))
                if "green" in colour:
                    maxGreen = max(maxGreen, get_val(colour, "green"))
                if "blue" in colour:
                    maxBlue = max(maxBlue, get_val(colour, "blue"))
        count += maxRed * maxGreen * maxBlue
    print(count)
    
if __name__ == "__main__":
    part_2()