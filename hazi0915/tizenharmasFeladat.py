# Tárolj el 2 számot egy-egy változóba, ami egy téglalap két oldala. Írd ki a téglalap kerületét és területét!

import beolvas

aoldal = beolvas.tortTeglalapBeolvas()
boldal = beolvas.tortTeglalapBeolvas()

teglalapkerulete = aoldal*2+boldal*2
teglalapterulete = float(aoldal)*float(boldal)

print("Kerület: ",teglalapkerulete)
print("Terület: ",teglalapterulete)