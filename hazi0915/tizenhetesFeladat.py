# Mentsd el egy változóba a vezetékneved, egy másikba a keresztneved, majd mentsd el a teljes nevedet egy teljesNev változóba, aztán írd ki!

import beolvas

szam1 = beolvas.vezetekNevBeolvas()
szam2 = beolvas.keresztNevBeolvas()
teljesNev = szam1+szam2

print("Teljes név: ",teljesNev)