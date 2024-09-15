# Tárolj el 3 számot egy-egy változóba! Írd ki a középső számot az értékük szerint összehasonlítva!

import beolvas

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()
szam3 = beolvas.tortSzamBeolvas()

# listába rendezés
szamok = [szam1,szam2,szam3]
szamok.sort()

print("Középső szám: ",szamok[1])