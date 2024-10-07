# 1.feladat
"""Pycharm fejlesztői környezetben készíts egy rövid programot, amely a felhasználótól bekéri a kör sugarát, és ennek alapján kiszámolja a kör kerületét és területét!
"""

PI = 3.14

megadott = input("kör sugara:  ")

sugar = int(megadott)

print("terület:")
print(sugar * sugar * PI, "cm2")

print("kerület:")
print(2 * sugar * PI, "cm")


