 #vstup pro uživatele
print("Vítejte v aplikaci pro výpočet obvodu obdelníku")
a= input ("zadejte promennou a:")
b= input ("zadejte promennou b:")
 #integer
a= int(a)
b= int(b)

if a>0 and b>0:
 #vzoreček + pravidlo
    vysledek = a*b
    print(f"vysledek je: {vysledek}")
 #poruší pravidla,dostane bídu
else:
    print("Tak jsi nadrbaný?")


    