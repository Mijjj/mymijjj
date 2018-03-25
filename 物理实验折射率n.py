import math
def calangleD(fi,fi1):
    angleD=0.5*((fi1-fi01)+(fi-fi0))
    return angleD

def angle2rad(ang):
    du=int(ang)
    fen=int((ang%1)*100)
    angle=du+(fen/60.0)
    return math.radians(angle)

def caln(a,d):
    n=math.sin((a+d)*0.5)/math.sin(a*0.5)
    return n
#===============================================

fi0=angle2rad(input ("fi0="))
print
fi01=angle2rad(input("fi01="))
print
angleA=angle2rad(input("angleA="))
print
i="y"
while i=="y":
    fi=angle2rad(input("fi="))
    print
    fi1=angle2rad(input("fi1="))
    print
    if math.degrees(calangleD(fi,fi1)) < 0:
        n=math.degrees(calangleD(fi,fi1))+360
    else:
        n=math.degrees(calangleD(fi,fi1))
    print n
    print
    print abs(caln(angleA,calangleD(fi,fi1)))
    print
    i=raw_input("continue? (y/n)")
