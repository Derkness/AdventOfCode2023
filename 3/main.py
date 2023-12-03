def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            lines.append([char for char in line])
    return lines

def is_symbol(char):
    return char not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]

def is_numeric(char):
    return char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def is_part_number(lines, lineIndex, charIndex, charLength):
    if (lineIndex != 0):
        for x in range (charIndex-charLength-1, charIndex + 1):
            if is_symbol(lines[lineIndex-1][x]):
                return True
            
    if is_symbol(lines[lineIndex][charIndex]):
        return True
    
    if charIndex-charLength-1 >= 0:
        if is_symbol(lines[lineIndex][charIndex-charLength-1]):
            return True
    
    if (lineIndex != len(lines)-1):
        for x in range (charIndex-charLength-1, charIndex + 1):
            if is_symbol(lines[lineIndex+1][x]):
                return True
    return False
        

def part_1():
    lines = get_input()
    count = 0
    for lineIndex, line in enumerate(lines):
        numberString=""
        for charIndex, char in enumerate(line):
            if is_numeric(char):
                numberString += char
            else:
                if (len(numberString) == 0):
                    continue
                count += int (numberString) if is_part_number(lines, lineIndex, charIndex, len(numberString)) else 0
                numberString = ""
            
            if (charIndex == len(line) - 1):
                if (len(numberString) == 0):
                    continue
                count += int (numberString) if is_part_number(lines, lineIndex, charIndex, len(numberString) - 1) else 0
                break
    print(count)

def get_connecting_numbers_in_line(line, connectingIndex, topOrBottom):
    numbers = [] # [number, startIndex (inclusive), endIndex (inclusive)]
    inNumber = False
    for charIndex, char in enumerate(line):
        if (char.isdigit()):
            if (not inNumber):
                numbers.append([char, charIndex, len(line)-1])
                inNumber = True
            else:
                numbers[-1][0] += char
        else:
            if (inNumber):
                numbers[-1][2] = charIndex - 1
                inNumber = False
    return [number for number in numbers if filter_connecting_only(number, connectingIndex, topOrBottom)]

def filter_connecting_only(value, connectingIndex, topOrBottom):
    if (topOrBottom):
        if (connectingIndex in range(value[1]-1, value[2]+2)):
            return True
    else:
        if value[1] == connectingIndex + 1:
            return True
        if value[2] == connectingIndex - 1:
            return True
    return False
    
                
def part_2():
    lines = get_input()
    count = 0
    for lineIndex, line in enumerate(lines):
        for charIndex, char in enumerate(line):
            if char == "*":
                relatedLines = []
                if (lineIndex > 0):
                    relatedLines.extend(get_connecting_numbers_in_line(lines[lineIndex-1], charIndex, True))
                    
                relatedLines.extend(get_connecting_numbers_in_line(line, charIndex, False))
                
                if (lineIndex < len(lines)-1):
                    relatedLines.extend(get_connecting_numbers_in_line(lines[lineIndex+1], charIndex, True))
                    
                if (len(relatedLines) == 2):
                    count += int(relatedLines[0][0]) * int(relatedLines[1][0])
    print(count)
                
                     
        
    
if __name__ == "__main__":
    part_2()