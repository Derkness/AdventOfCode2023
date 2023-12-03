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

def get_connecting_numbers_in_line(line, connectingIndex):
    numbers = [] # [number, startIndex (inclusive), endIndex (inclusive)]
    for charIndex, char in enumerate(line):
        if (char.isdigit()):
            numberString += char
        else
    
                
def part_2():
    lines = get_input()
    count = 0
    for lineIndex, line in enumerate(lines):
        for charIndex, char in enumerate(line):
            if char is "*":
                
        
    
if __name__ == "__main__":
    part_2()