# Ments el egy számot szövegként egy változóba, majd egy másik változóba egy egész számot. Majd írd ki az összegüket.

import beolvas

szam1 = beolvas.szovegSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()
szam3 = int(szam1)+szam2

print("Eredmény: ",szam3)