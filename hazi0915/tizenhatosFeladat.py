# Tárolj el 2 számot egy-egy változóba, melyek egy derékszögű háromszög befogói. Mekkora a harmadik oldalt?

import beolvas

szam1 = beolvas.tortHaromszogBeolvas()
szam2 = beolvas.tortHaromszogBeolvas()
szam3 = (szam1**2+szam2**2)**0.5

print("Átfogó: ",(szam3))

