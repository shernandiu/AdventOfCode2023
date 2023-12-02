import re
from math import prod

DEBUG = False

if DEBUG:
    text = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
else:
    with open("input/day2", "r") as f:
        text = f.read()


# Part 1
avail_cubes = {'red': 12,  'green': 13, 'blue': 14}

games = []
for line in text.splitlines():
    cubes = {}
    for num, color in re.findall(r"(\d+) (\w+)", line):
        cubes[color] = max(cubes.get(color, 0), int(num))
    games.append(cubes)

p1 = sum(i+1 for i, game in enumerate(games) if all(game.get(color) <= avail_cubes[color] for color in avail_cubes))
print("Part 1:", p1)

# Part 2
p2 = sum(prod(game.values()) for game in games)
print("Part 2:", p2)
