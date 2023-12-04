def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
           lines.append(line.strip())
    return lines

def part_1():
    lines = get_input()
    count = 0
    for line in lines:
        [_, game] = line.split(":")
        [winners, guesses] = [x.split() for x in game.split("|")]
        winningGuesses = 0
        for guess in guesses:
            winningGuesses += 1 if guess in winners else 0
        count += pow(2, winningGuesses-1) if winningGuesses > 0 else 0
    
    print(count)
    
if __name__ == "__main__":
    part_1()