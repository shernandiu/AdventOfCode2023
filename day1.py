import re
test = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
# with open("input/day1", "r") as f:
#     test = f.read()

def count(text):
    text = re.sub(r"[^\d|\n]", "", text)
    return sum([int(line[0] + line[-1]) for line in text.splitlines() if line])

print(f"Part 1: {count(test)}")
for i,j in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
    i = str(i+1)
    test = test.replace(j, j+i+j)
print(f"Part 2: {count(test)}")
