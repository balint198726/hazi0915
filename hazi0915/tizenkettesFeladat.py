# Tárolj el egy egész számot egy változóba, ami egy kör átmérője. Írd ki a kör kerületét és területét!
import beolvas

Atmero = beolvas.egeszKorBeolvas()
korkerulete = int(Atmero)*3.14
korterulete = int(Atmero)/2**2*3.14

print("Kerület: ",korkerulete)
print("Terület: ",korterulete)