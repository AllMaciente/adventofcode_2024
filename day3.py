import re

from utils import get_puzzle_input

puzzleInput = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# puzzleInput = get_puzzle_input.get_input("https://adventofcode.com/2024/day/3/input")

lines = puzzleInput.strip().split("\n")

# print(lines)


def extractMul(text):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    result = re.findall(pattern, text)

    listResult = [(int(x), int(y)) for x, y in result]

    return listResult


allSumMul = 0

for line in lines:
    mulList = extractMul(line)
    for mul in mulList:
        allSumMul += mul[0] * mul[1]


print(allSumMul)
