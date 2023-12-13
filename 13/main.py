def get_input():
    games=[]
    game = []
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) == 0):
                games.append(game)
                game = []
            else:
                game.append(strippedLine)
    games.append(game)
    return games

def is_horizontal_mirror(a, b, lines):
    while a >= 0 and b < len(lines):
        if (lines[a] != lines[b]):
            return False
        a-=1
        b+=1
    return True

def is_vertical_mirror(a, b, line):
    while a >= 0 and b < len(line):
        if (line[a] != line[b]):
            return False
        a-=1
        b+=1
    return True

def part_1():
    horizontalLineRows = 0
    verticalLineRows = 0
    games = get_input()
    for game in games:
        for index in range(len(game)-1):
            if game[index + 1] == game[index]:
                a = index + 1
                b = index
                if is_horizontal_mirror(a, b, game):
                    horizontalLineRows += index + 1
        possibleMirrors = [True] * (len(game[0]) - 1)
        # possibleMirrors[-1] = False
        for line in game:
            for index in range(len(line)-1):
                if line[index + 1] == line[index]:
                    a = index + 1
                    b = index
                    if not is_vertical_mirror(a, b, line):
                        possibleMirrors[index] = False
                else:
                    possibleMirrors[index] = False
        for index, mirror in enumerate(possibleMirrors):
            if (mirror is True):
                verticalLineRows += index + 1
    
    print(verticalLineRows + horizontalLineRows * 100)
    
def compare_strings_with_1_tolerance(s1, s2):
    foundOne = False

    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if foundOne:
                return False
            else:
                foundOne = True

    return True

def is_horizontal_mirror_2(a, b, lines, repaired = False):
    while b >= 0 and a < len(lines):
        if (lines[a] != lines[b]):
            if repaired:
                return False
            repaired = True
            if not compare_strings_with_1_tolerance(lines[a], lines[b]):
                return False
        a+=1
        b-=1
    return repaired # It has to have been repaired once

def is_vertical_mirror_2(a, b, line, usedRepair, index):
    while b >= 0 and a < len(line):
        if line[a] != line[b]:
            if usedRepair[index]:
                return False
            usedRepair[index] = True
        a+=1
        b-=1
    return usedRepair[index] # It has to have been repaired once

def part_2():
    horizontalLineRows = 0
    verticalLineRows = 0
    games = get_input()
    for game in games:
        for index in range(len(game)-1):
            if game[index + 1] == game[index]:
                a = index + 1 + 1
                b = index - 1
                if is_horizontal_mirror_2(a, b, game):
                    horizontalLineRows += index + 1
            elif compare_strings_with_1_tolerance(game[index + 1], game[index]):
                a = index + 1 + 1
                b = index - 1
                if is_horizontal_mirror_2(a, b, game, True):
                    horizontalLineRows += index + 1
        game=[*zip(*game)]
        for index in range(len(game)-1):
            if game[index + 1] == game[index]:
                a = index + 1 + 1
                b = index - 1
                if is_horizontal_mirror_2(a, b, game):
                    verticalLineRows += index + 1
            elif compare_strings_with_1_tolerance(game[index + 1], game[index]):
                a = index + 1 + 1
                b = index - 1
                if is_horizontal_mirror_2(a, b, game, True):
                    verticalLineRows += index + 1
        # possibleMirrors = [True] * (len(game[0]) - 1)
        # usedRepair = [False] * (len(game[0]))
        # for line in game:
        #     for index in range(len(line)-1):
        #         if line[index + 1] == line[index]:
        #             a = index + 1 + 1
        #             b = index - 1
        #             if not is_vertical_mirror_2(a, b, line, usedRepair, index):
        #                 possibleMirrors[index] = False
        #         elif not usedRepair[index] and compare_strings_with_1_tolerance(line[index + 1], line[index]):
        #             usedRepair[index] = True
        #             a = index + 1 + 1
        #             b = index - 1
        #             if not is_vertical_mirror_2(a, b, line, usedRepair, index):
        #                 possibleMirrors[index] = False
        #         else:
        #             possibleMirrors[index] = False
        # # print(usedRepair)
        # # print(possibleMirrors)
        # # print('---')
        # for index, mirror in enumerate(possibleMirrors):
        #     if (mirror is True and usedRepair[index] is True):
        #         verticalLineRows += index + 1
    
    print(verticalLineRows + horizontalLineRows * 100)
            
    
if __name__ == "__main__":
    part_2()
    
    # Too high:
    # 40000
    
    # Too low:
    # 35000
    
    # Wrong for unknown reason:
    # 38815
    # 38904
    
    # RIGHT ANSWER: 39037