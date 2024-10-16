"""2. Feladat - \
Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 5 x 5-ös mezőben az alábbi alakzatot!"""

# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print("O", end='')
#         else:
#             print(".", end='')
#     print()

"""3. Feladat - X
Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 7 x 7-es mezőben az alábbi alakzatot!"""

size = int(input("Add meg a méretet! "))

for i in range(size):
    for j in range(size):
        if i == j:
            print("0", end=' ')
        elif i+j == size -1:
            print("O", end=' ')
        else:
            print(".", end=' ')
    print()
