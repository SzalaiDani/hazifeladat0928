# 9.	Írasd ki az első 7 pozitív egész számot vesszővel elválasztva!
    # a.	úgy, hogy a végén ne legyen vessző!
import beolvas

def elsoPozitiv():
    for i in range(1, 8):
        print(i, end=" ")

def elsoPozitivA():
    szamok = list(range(1,8))

    print(', '.join(map(str, szamok)))
