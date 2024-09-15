# 5.	Tárolj el két számot egy-egy változóba! Írd ki az összegüket, különbségüket, szorzatukat és hányadosukat, hatványukat!
import beolvas

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()

# muveletek
osszeg = szam1 + szam2
kulonbseg = szam1-szam2
szorzat = szam1*szam2
hanyados = szam1*szam2
hatvany = szam1**szam2
maradek = szam1 % szam2

# kiiras
print(osszeg)
print(kulonbseg)
print(szorzat)
print(hanyados)
print(maradek)
print(hatvany)