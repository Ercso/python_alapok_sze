"""5. Feladat
Írj egy programot, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó."""

folyt = False

while folyt == False:
    fsz_input = int(input("Kérlek adj meg egy számot! "))
    if fsz_input % 2 == 0:
        folyt = True
        print("Szép volt!")

"""6. Feladat
Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot! A képernyőre kizárólag csak a 3-mal oszthatóakat írja ki, és a végén informálja a felhasználót arról is, hány darab ilyen szám volt."""

