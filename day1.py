from utils import get_puzzle_input

puzzleInput = get_puzzle_input.get_input("https://adventofcode.com/2024/day/1/input")
# puzzleInput = """"
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# """

rightList = []
leftList = []

for linha in puzzleInput.strip().split("\n"):
    partes = linha.split()
    if len(partes) == 2:  # Garante que há exatamente dois valores
        num1, num2 = partes
        rightList.append(int(num1))
        leftList.append(int(num2))
    else:
        print(f"Linha ignorada (não tem exatamente dois valores): {linha}")

rightList.sort()
leftList.sort()

totalDistancia = []

for i in range(len(rightList)):
    totalDistancia.append(abs(rightList[i] - leftList[i]))

print(sum(totalDistancia))