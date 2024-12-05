puzzleInput = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

from utils import get_puzzle_input

puzzleInput = get_puzzle_input.get_input("https://adventofcode.com/2024/day/5/input")

rawRules, rawOrder = puzzleInput.strip().split("\n\n")
rawSplitRules = rawRules.split("\n")
Rules = {}

for rule in rawSplitRules:
    X, Y = rule.split("|")
    if not X in Rules:
        Rules[X] = []
    Rules[X].append(Y)

# print(Rules, "----", sep="\n")

rawSplitOrder = rawOrder.split("\n")
Orders = [tuple(x.split(",")) for x in rawSplitOrder]
# print(rawOrder, "----", sep="\n")
# print(rawSplitOrder, "----", sep="\n")
# print(Orders, "----", sep="\n")


def checkOrder(order):
    # print("order", order)
    for page in order:
        # print("page", page)
        for i in order:
            # print("i", i)
            if i == page:
                break
            if not page in Rules:
                break
            for j in Rules[page]:
                # print("j", j)
                if i == j:
                    # print("false")
                    return False
    # print("true")
    return True


wrongOrder = []
rightOrder = []
for order in Orders:
    if checkOrder(order):
        rightOrder.append(order)
    else:
        wrongOrder.append(order)


# print(rightOrder, "----", sep="\n")
def middlePageSum(order):
    middlePage = 0
    for i in order:
        middlePage += int(i[len(i) // 2])
    return middlePage


print(middlePageSum(rightOrder))

# part 2


def updateOrder(order):
    newOrder = []  # Lista que vai armazenar a ordem correta
    for page in order:
        inserted = False
        for i in range(len(newOrder)):
            # Se o elemento page deve vir antes de newOrder[i], o insere
            if page in Rules and newOrder[i] in Rules[page]:
                newOrder.insert(i, page)
                inserted = True
                break
        # Se o elemento não foi inserido em nenhuma posição, é colocado no final
        if not inserted:
            newOrder.append(page)
    return newOrder


# Testando a função para as ordens incorretas
newWrongOrder = []

for i in wrongOrder:
    newWrongOrder.append(updateOrder(i))

# print(newWrongOrder)

print(middlePageSum(newWrongOrder))
