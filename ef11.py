# 11.	Írasd ki 2 bekért szám (x és y) alapján, hogy mennyi 3x+y2!
import beolvas

def xy():
    x = beolvas.intbeolvas()
    y = beolvas.intbeolvas()

    keplet = (3*x) + (y**2)

    print(keplet)