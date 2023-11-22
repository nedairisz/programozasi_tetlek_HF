

# Számold meg, hogy hány darab 7-tel osztható szám van 1-1000 között!
def feladat1():
    i:int = 1
    szamlalo:int = 0
    while i<=1000:
        if i%7 == 0:
            szamlalo += 1
        i+=1
    return szamlalo

# Számold meg, hogy hány darab 12-vel osztható szám van 2000-20000 között!
def feladat2():
    i:int = 2000
    szamlalo:int =0
    while i<=20000:
        if i%12==0:
            szamlalo+=1
        i+=1
    return szamlalo

# Írd ki az első 20 3-mal osztható szám négyzetének összegét!
def feladat3():
    i:int=0
    osszeg:int=0
    szamlalo:int=0
    while szamlalo<=20:
        if i%3==0:
            osszeg+=i**2
            szamlalo+=1
        i+=1
    print(osszeg)

# Keresd meg egy szám egész osztóit!
def feladat4(szam:int):
    i:int=1
    gyujto:int=[]
    while i<=szam:
        if szam%i==0:
            # gyujto.append(i)
            gyujto+= [i]
        i+=1
    print(gyujto)

# Keresd meg egy szám legnagyobb egész osztóját!
def feladat5(szam:int):
    i:int =1
    legnagyobb_oszto:int = 1
    while i<szam:
        if szam%i==0:
            if i > legnagyobb_oszto:
                legnagyobb_oszto=i
        i+=1
    print(legnagyobb_oszto)


# Vizsgáljuk meg, hogy egy adott szám prímszám-e!
# Az internetről szedtem:(
"""def feladat6(szam:int):
    vanoszto = False
    oszto = 2
    while oszto < szam and not vanoszto:
        if szam % oszto == 0:
            vanoszto = True
        oszto += 1

    if vanoszto:
        print(f"{szam} nem prim szam!")
    else:
        print(f"{szam} prim szam!")"""
    
def prim(x:int):
    if x<=1:
        print("Nem prím szám")
    elif x==2:
        print("A 2 az egy prím szám")
    else:
        oszto_db= 0
        for i in range(3,x-1,1):
            if(x%i==0):
                oszto_db+=1
                
        if oszto_db==0:
            print(f"{x} prím")
        else:
            print(f"{x} nem prím")


# Számold meg, hogy hány négyzetszám van 0-100000 között!
def feladat7():
    i:int =0
    szamlalo:int =0
    while i<=100000:
        if i%3==0 or i%3==1:
            szamlalo+=1
        i+=1
    print(f" 0-100000 között {szamlalo} db négyzetszám van!")

# Számold meg, hogy hány négyzetszám van 10000-100000 között!
def feladat8():
    i: int = 10000
    szamlalo: int = 0
    while i <= 100000:
        if i % 3 == 0 or i % 3 == 1:
            szamlalo += 1
        i += 1
    print(f" 10000-100000 között {szamlalo} db négyzetszám van!")

# Add össze, hogy mennyi a 0-10000 közötti négyzetszámok összege!
def feladat9():
    i:int =0
    gyujto:int =0
    while i<=100000:
        if i%3==0 or i%3==1:
            gyujto+=i
        elif i%4==0 or i%4==1:
            gyujto += i
        elif i%5==0 or i%5==1:
            gyujto += i
        i+=1
    print(f"A 0-100000 közötti négyzetszámok osszege {gyujto}.")
