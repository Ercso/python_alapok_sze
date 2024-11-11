"""Készítsünk programot, amely dinnyék csomagolásához végez számításokat. A
dinnyéket szalaggal kell átkötni úgy, hogy kétszer körbe érje őket, és a masni
készítéséhez számolunk még 60 cm-t. A program kérje be a dinnye átmérőjét, a
dinnyék számát, és a rendelkezésre álló szalag hosszát! Számítsa ki, és írja a
képernyőre, hogy a bekért számú dinnye csomagolásához hány méter szalagra van
szükség, valamint állapítsa meg, hogy elegendő szalagunk van-e a művelet
elvégzéséhez, és ezt is közölje a felhasználóval!"""

def a_feladat():
    dinnye_at = float(input("Kérlek add meg a dinnye átmérőjét (m-ben)! "))
    dinnye_db = float(input("Kérlek add meg a dinnye db számát! "))
    szalag = float(input("Kérlek add meg a szalag hosszát (m-ben)! "))

    p  = 3.14

    kor = dinnye_at * p
    szalag_kell = dinnye_db * kor + 0.6
    print(f"A csomagoláshoz szükséges szalag: {szalag_kell}")

    if szalag_kell <= szalag:
        print("Elegendő szalagod van!")
    else:
        print("Szükséged van még szalagra!")


a_feladat()