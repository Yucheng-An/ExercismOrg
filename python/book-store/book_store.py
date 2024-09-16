# def allBookNoDis(booksCounter):
#     money = 0
#     for i in booksCounter:
#         money += i * 800
#     booksCounter = [0] * 5
#     return money, booksCounter
#
#
# def twoDiff(booksCounter, f, s):
#     booksCounter[f] = booksCounter[f] - 1
#     booksCounter[s] = booksCounter[s] - 1
#     money = int(2 * 800 * 0.95)
#     return money, booksCounter
#
# def threeDiff(booksCounter, f, s, t):
#     booksCounter[f] = booksCounter[f] - 1
#     booksCounter[t] = booksCounter[t] - 1
#     booksCounter[s] = booksCounter[s] - 1
#     money = int(3 * 800 * 0.90)
#     return money, booksCounter
#
# def fourDiff(booksCounter, f, s, t, f1):
#     booksCounter[f] = booksCounter[f] - 1
#     booksCounter[s] = booksCounter[s] - 1
#     booksCounter[t] = booksCounter[t] - 1
#     booksCounter[f1] = booksCounter[f1] - 1
#     money = int(4 * 800 * 0.80)
#     return money, booksCounter
#
# def fiveDiff(booksCounter):
#     booksCounter[0] = booksCounter[0] - 1
#     booksCounter[1] = booksCounter[1] - 1
#     booksCounter[2] = booksCounter[3] - 1
#     booksCounter[4] = booksCounter[4] - 1
#     booksCounter[5] = booksCounter[5] - 1
#     money = int(4 * 800 * 0.75)
#     return money, booksCounter
#
# def total(basket):
#     booksCounter = [0] * 5
#     for i in basket:
#         booksCounter[i - 1] += 1
#
#     print(booksCounter)
#
#
# total([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2])

from collections import Counter


def total(basket):
    A = sorted(Counter(basket).values(), reverse=True)
    if 4 < len(A): A.append(min(A[2] - A[3], A[4]))
    B = [800, 720, 640, 400, 440, -40]
    return sum(A * B for (A, B) in zip(A, B))
