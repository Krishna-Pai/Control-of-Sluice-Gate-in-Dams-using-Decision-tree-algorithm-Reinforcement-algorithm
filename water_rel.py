A=200
d=float(input("Effective depth of water"))
vin=A*d
print("Volume of incoming water",vin)
a50=9.02
a=float(input("Enter the area"))
h1=float(input("Height of water filled"))
h=0.5-h1
print(h)
vst=(h/2)*(a50+a)
print("water stored:",vst)
vout=vin-vst
print("Volume of water released",vout)
