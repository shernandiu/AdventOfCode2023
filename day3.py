import re
from collections import defaultdict
from math import prod
from itertools import product

DEBUG = False
if DEBUG:
    text = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
else:
    with open("input/day3.txt", "r") as f:
        text = f.read()
text = text.splitlines()

def check_symbol(i: int, j: int) -> tuple[int, int]:
    for x, y in product((i-1, i, i+1), (j-1, j, j+1)):
        if not 0 <= x < len(text) or not 0 <= y < len(text[0]):
            continue
        if re.match(r"[^\d\.]", text[x][y]):
            return (x, y)
    return None

gears: defaultdict[tuple[int, int], list[int]] = defaultdict(list)
for i, line in enumerate(text):
    for number in re.finditer(r'\d+', line):
        symbol = next((aux for j in range(number.start(), number.end()) 
                       if (aux:=check_symbol(i,j)) is not None), None)
        if symbol: 
            gears[symbol].append(int(number.group()))

p1 = sum(sum(p) for p in gears.values())
p2 = sum(prod(x) for [i, j], x in gears.items() if len(x) == 2 and text[i][j] == '*')

if DEBUG: 
    assert p1 == 4361,   "Test 1 error"
    assert p2 == 467835, "Test 2 error"
    
print("Part 1:", p1)
print("Part 2:", p2)
