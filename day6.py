puzzleInput = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

lines = puzzleInput.strip().split("\n")
grid = [list(char) for char in lines]


def findGuard(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] in ("^", ">", "V", "<"):
                return (x, y,grid[x][y])


def move(grid):
    pos = findGuard(grid)
    if  pos[3] == "^":
        

