from utils import get_puzzle_input

puzzleInput = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
# puzzleInput = get_puzzle_input.get_input("https://adventofcode.com/2024/day/2/input")
lista = []
reportsSafe = 0
a = puzzleInput.strip().split("\n")
for i in a:
    lista.append(i.split())
# print(a)
# print(lista)


def isSafe(i):
    check = 0
    if i[0] < i[1]:
        for j in range(1, len(i)):
            if (int(i[j]) - int(i[j - 1])) <= 3 and (int(i[j]) - int(i[j - 1])) >= 1:
                check += 1
            else:
                return False

    elif i[0] > i[1]:
        for j in range(1, len(i)):
            if (int(i[j - 1]) - int(i[j])) <= 3 and (int(i[j - 1]) - int(i[j])) >= 1:
                check += 1
            else:
                return False
    else:
        return False
    
    return check >=len(i) -1


for i in lista:
    if isSafe(i):    
        reportsSafe += 1
    
    for j in  range(1,len(i) - 1):
        modifiedReport = i[:j] + [j+1:]
    
print(reportsSafe)
