import math
pi = math.pi
perc= input("Percentage of close gate\n")
h=50
diam = 8
G = 9.810*math.pow(10,-6)
radius=diam/2
p = float(perc/100.00)
if(perc<=50):
    x = (radius - p*diam)
    A = math.acos(x/radius)
    A = math.degrees(A)
else:
    x = (p*diam-radius)
    T = math.acos(x/radius)
    T = math.degrees(T)
    A = (360 - (2*T))/2
A=math.radians(A)
P1 = G*radius*radius
P2 = (h+radius)*(A-math.sin(A)*math.cos(A))
P3 = 0.66*radius*math.pow((math.sin(A)),3)
P = P1 * (P2 - P3)
P = P *math.pow(10,3)
print(P)
