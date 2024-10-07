#1. Feladat
""""Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót."""

#x = int(input("adj egy egesz szamot! "))
#if x % 2 == 0 and x > 0:
#    print('a szam paros and pozitiv')
#elif x % 2 != 0 and x < 0:
#    print('a szam paratlan and negative')

#2. Feladat
"""Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi, hogy az ikrek (Henrik és Hanna) jönnek-e ma kosrazni! Például így: Jön Henrik ma kosarazni? (i/n). A program írja ki, hogy melyik állítás igaz az alábbiak közül:
- egyikük sem jön kosarazni,
- mind a ketten jönnek kosarazni,
- csak az egyikük jön kosarazni."""

hanna = input("Hanna jon ballingolni(i/n)? ")
henrick = input("Henrick jon ballolni(i/n)? ")
if henrick == "n" and hanna == "i":
    print("Egyikojuk jon kosarazni.")
elif henrick == "i" and hanna == "n":
    print("Egyikojuk jon kosarazni.")
elif henrick and hanna == "i":
    print("Mind2-en jonnek.")
elif henrick and hanna == "n":
    print("Nem szeretnek teged, sajnalom. :(")