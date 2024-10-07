# 1 Feladat
#"""Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!"""

#kedv = (input("Jo napod van oreg? "))
#kedv_lowercase = kedv.lower()
#if kedv_lowercase == "ja" :
#    print("akkor remelem nem sokaig")
#else:
#    print('remeltem is')
#print("a program vege")

# 2 Feladat
"""Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"""


kedv = (input("Jo napod van oreg? "))
kedv_lowercase = kedv.lower()
if kedv_lowercase == "ja" :
    print("akkor remelem nem sokaig")
elif kedv_lowercase == "nem" :
    print("remeltem is")
else:
    print('nem ertem a valaszt')
print("a program vege")

# 3. Feladat
"""Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb."""

import random
random_number = random.radiant(a:1 b:5)
number = int(input("Gondoltam egy számra!"))
print(f"Erre gondoltam: {random_number}")

if random_number == number:
    print("talalt")
else:
    print("nem ez volt")

