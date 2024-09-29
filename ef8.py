# 7.	Kérj be 2 számot, majd írasd ki a számokat 0-tól a 2 szám szorzatáig!
# 8.	Írd meg a fenti feladatot while és for ciklussal is!
import beolvas

def szorzatSorozatFor():

    szam1 = beolvas.intbeolvas()
    szam2 = beolvas.intbeolvas()

    szorzat = szam1 * szam2

    for i in range(0, szorzat+1):
        print(i, end=" ")

def szorzatSorozatWhile():

    szam1 = beolvas.intbeolvas()
    szam2 = beolvas.intbeolvas()

    szorzat = szam1 * szam2

    n = -1
    while n != szorzat:
        n += 1
        print(n, end=" ")