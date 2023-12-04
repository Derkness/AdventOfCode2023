def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
           lines.append(line.strip())
    return lines

def get_winning_numbers(guesses, winners):
    winningGuesses = 0
    for guess in guesses:
        winningGuesses += 1 if guess in winners else 0
    return winningGuesses
    

def part_1():
    lines = get_input()
    count = 0
    for line in lines:
        [_, game] = line.split(":")
        [winners, guesses] = [x.split() for x in game.split("|")]
        winningGuesses = get_winning_numbers(guesses, winners)
        count += pow(2, winningGuesses-1) if winningGuesses > 0 else 0
    
    print(count)
    

def part_2():
    lines = get_input()
    extraCards = {}
    for line in lines:
        [cardName, card] = line.split(":")
        cardId = int(cardName.replace("Card ",""))
        [winners, guesses] = [x.split() for x in card.split("|")]
        
        winningNumbers = get_winning_numbers(guesses, winners)
        for i in range(1, winningNumbers+1):
            extraCards.update({cardId + i: extraCards.get(cardId + i, 0) + extraCards.get(cardId, 0) + 1 })
            
    print(sum(extraCards.values()) + len(lines))
        
if __name__ == "__main__":
    part_2()
    
# too low 65083
# right answer 5329815!