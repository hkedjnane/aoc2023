import sys
from functools import cmp_to_key

fiveoak = [5]
fouroak = [1,4]
fh = [2,3]
toak = [1,1,3]
tp = [1,2,2]
op = [1,1,1,2]
high = [1,1,1,1,1]

order = [high, op, tp, toak, fh, fouroak, fiveoak]


card_strength = {
    '2' : 0,
    '3' : 1,
    '4' : 2,
    '5' : 3,
    '6' : 4,
    '7' : 5,
    '8' : 6,
    '9' : 7,
    'T' : 8,
    'J' : 9,
    'Q' : 10,
    'K' : 11,
    'A' : 12
}

def treat_input(line):
    hand, score = line.strip().split(' ')
    return hand, int(score)

def get_type(hand):
    hand_amount = [0] * len(card_strength)
    for c in hand:
        hand_amount[card_strength[c]] += 1
    hand_amount = sorted(filter(None, hand_amount))
    for i in range(len(order)):
        type = order[i]
        if type == hand_amount:
            return i



def sort_hands(hand1, hand2):
    hand1, _ = hand1
    hand2, _ = hand2
    t1, t2 = get_type(hand1), get_type(hand2)
    if (t1 < t2):
        return -1
    if (t1 > t2):
        return 1
    for i in range(len(hand1)):
        v1 = card_strength[hand1[i]]
        v2 = card_strength[hand2[i]]
        if (v1 < v2):
            return -1
        if (v1 > v2):
            return 1
    return 0
            

def main(argv, argc):
    hands = sorted(list(map(treat_input,open(argv[1]).readlines())), key = cmp_to_key(sort_hands))
    total = 0
    for i in range(len(hands)):
        _, bet = hands[i]
        total += bet * (i + 1)
    print(total)



if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
