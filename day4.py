puzzleInput = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

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
