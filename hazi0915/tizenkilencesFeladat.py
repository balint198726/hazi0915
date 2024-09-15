# Tárolj el egy kétjegyű egész számot egy változóba! Írd ki a számjegyek összegét!

import beolvas

szam1 = beolvas.egeszketSzamBeolvas()
tizek = szam1 // 10
egyek = szam1 % 10

szam2 = tizek + egyek

print("A számjegyek összege: ",szam2)