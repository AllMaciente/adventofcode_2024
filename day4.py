puzzleInput = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""

from utils import get_puzzle_input

puzzleInput = get_puzzle_input.get_input("https://adventofcode.com/2024/day/4/input")


lines = puzzleInput.strip().split("\n")
grid = [list(line) for line in lines]


def countWord(grid, word):
    rows, cols = len(grid), len(grid[0])
    wordLen = len(word)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    word.upper()

    def validPos(x, y):
        return 0 <= x < rows and 0 <= y < cols

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                for dx, dy in directions:
                    x, y = i, j
                    for _ in range(wordLen):
                        if not validPos(x, y):
                            break
                        if grid[x][y] != word[_]:
                            break
                        x, y = x + dx, y + dy
                    else:
                        count += 1

    return count


print(countWord(grid, "XMAS"))

# part 2


def countXPattern(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    patterns = [
        [
            (-1, -1, "M"),
            (1, -1, "M"),
            (-1, 1, "S"),
            (1, 1, "S"),
        ],
        [
            (-1, -1, "M"),
            (1, -1, "S"),
            (-1, 1, "M"),
            (1, 1, "S"),
        ],
        [
            (-1, -1, "S"),
            (1, -1, "M"),
            (-1, 1, "S"),
            (1, 1, "M"),
        ],
        [
            (-1, -1, "S"),
            (1, -1, "S"),
            (-1, 1, "M"),
            (1, 1, "M"),
        ],
    ]

    def checkPattern(x, y, pattern):
        for dx, dy, char in pattern:
            if not validPos(x + dx, y + dy):
                return False
            if grid[x + dx][y + dy] != char:
                return False
        return True

    def validPos(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "A":
                for pattern in patterns:
                    if checkPattern(i, j, pattern):
                        count += 1

    return count


print(countXPattern(grid))
