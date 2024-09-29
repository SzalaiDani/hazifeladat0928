# 12.	Számold meg 2 bekért szám közötti páros számokat! (pl. hány db páros szám van 4 és 31 között?)
import beolvas

def parosSzamok():
    szam1 = beolvas.intbeolvas()
    szam2 = beolvas.intbeolvas()
    szamlalo = 0

    szamok = [szam1, szam2]
    szamok.sort()

    for i in range(szamok[0]+1, szamok[1]):
        if i % 2 == 0:
            szamlalo += 1
            print(i, end=" ")
    print("\nAz összes páros szám: "+str(szamlalo))

