import re

DEBUG = False
if DEBUG:
    text = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
else:
    with open("input/day4.txt", "r") as f:
        text = f.read()
text = text.splitlines()

winning_numbers = [[{int(x) for x in re.findall(r"(\d+)(?!.*:)", l)}
                    for l in line.split('|')] for line in text]

p1 = sum(2**(common-1)
         for w, n in winning_numbers if (common := len(w & n)) > 0)

numb_cards = [1]*len(text)
for i, (w, n) in enumerate(winning_numbers):
    for j in range(len(w & n)):
        numb_cards[i+j+1] += numb_cards[i]
p2 = sum(numb_cards)

if DEBUG:
    assert p1 == 13
    assert p2 == 30

print("Part 1:", p1)
print("Part 2:", p2)
