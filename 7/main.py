from functools import cmp_to_key

PossibleCards1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
PossibleCards2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

def get_input():
    lines=[]
    with open("input.txt", "r") as file:
        for line in file:
            strippedLine = line.strip()
            if (len(strippedLine) > 0):
                lines.append(strippedLine.split())
    return lines

# 1, 2, 3, 4, 5, 6, or 7
def get_hand_type_index1(hand):
    if len(set(hand)) == len(hand):
        return 1
    if len(set(hand)) == len(hand) - 1:
        return 2
    if len(set(hand)) == len(hand) - 2:
        for possibleCard in PossibleCards1:
            if (hand.count(possibleCard) > 2):
                return 4
        return 3
    if len(set(hand)) == len(hand) - 3:
        for possibleCard in PossibleCards1:
            if (hand.count(possibleCard) > 3):
                return 6
        return 5
    if (len(set(hand)) == 1):
        return 7
    
    raise Exception("Sorry, no hand type found")

def compare1(x, y):
    hand1 = x[0]
    hand2 = y[0]
    handType1 = get_hand_type_index1(hand1)
    handType2 = get_hand_type_index1(hand2)
    if (handType1 != handType2):
        return handType1-handType2
    for i in range(len(hand1)):
        if PossibleCards1.index(hand1[i]) != PossibleCards1.index(hand2[i]):
            return PossibleCards1.index(hand1[i]) - PossibleCards1.index(hand2[i])
    return 0

def part_1():
    lines = get_input()
    sortedLines = sorted(lines, key=cmp_to_key(compare1))
    for x in sortedLines:
        print(x[0], get_hand_type_index1(x[0]))
    count = 0
    for i, line in enumerate(sortedLines):
        count+=(i+1)*int(line[1])
    print(count)
    
def get_most_common(hand):
    localPossibleCards = PossibleCards2[1:][::-1]
    rankings = [hand.count(x) for x in localPossibleCards]
    lowestIndex = max(range(len(rankings)), key=rankings.__getitem__)
    return localPossibleCards[lowestIndex]
    

# 1, 2, 3, 4, 5, 6, or 7
def get_hand_type_index2(hand):
    newHand = hand.replace("J",get_most_common(hand))
    print(hand,"->",newHand)
    if len(set(newHand)) == len(newHand):
        return 1
    if len(set(newHand)) == len(newHand) - 1:
        return 2
    if len(set(newHand)) == len(newHand) - 2:
        for possibleCard in PossibleCards2:
            if (newHand.count(possibleCard) > 2):
                return 4
        return 3
    if len(set(newHand)) == len(newHand) - 3:
        for possibleCard in PossibleCards2:
            if (newHand.count(possibleCard) > 3):
                return 6
        return 5
    if (len(set(newHand)) == 1):
        return 7
    
    raise Exception("Sorry, no hand type found")

def compare2(x, y):
    hand1 = x[0]
    hand2 = y[0]
    handType1 = get_hand_type_index2(hand1)
    handType2 = get_hand_type_index2(hand2)
    if (handType1 != handType2):
        return handType1-handType2
    for i in range(len(hand1)):
        if PossibleCards2.index(hand1[i]) != PossibleCards2.index(hand2[i]):
            return PossibleCards2.index(hand1[i]) - PossibleCards2.index(hand2[i])
    return 0

def part_2():
    lines = get_input()
    sortedLines = sorted(lines, key=cmp_to_key(compare2))
    count = 0
    for i, line in enumerate(sortedLines):
        count+=(i+1)*int(line[1])
    print(count)
    
if __name__ == "__main__":
    part_2()
    