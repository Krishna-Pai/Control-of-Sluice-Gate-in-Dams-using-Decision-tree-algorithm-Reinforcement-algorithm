P = 26.627636677
p = input("Enter Water Pressure")
perc = 100 * p / P
print(perc)
if(perc>50):
    print("Doors Open")
else:
    print("Doors close")
