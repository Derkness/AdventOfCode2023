import math


def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append(strippedLine)
    return lines

def part_1():
    lines = get_input()
    [_, times] = [x.split() for x in lines[0].split(":")]
    [_, distances] = [x.split() for x in lines[1].split(":")]
    races = len(times)
    count = 1
    
    for raceId in range(races):
        raceTime = int(times[raceId])
        raceDistance = int(distances[raceId])
        wins = 0
        for chargeTime in range(raceTime):
            travelled = chargeTime*(raceTime-chargeTime)
            wins += travelled > raceDistance
        count *= wins
    print(count)

def part_2():
    lines = get_input()
    [_, times] = [x.split() for x in lines[0].split(":")]
    [_, distances] = [x.split() for x in lines[1].split(":")]
    
    raceTime = int("".join(times))
    raceDistance = int("".join(distances))
    wins = 0
    for chargeTime in range(raceTime):
        travelled = chargeTime*(raceTime-chargeTime)
        wins += travelled > raceDistance
    print(wins)
            
if __name__ == "__main__":
    part_2()