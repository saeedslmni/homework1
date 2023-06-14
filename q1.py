inlet1=[0,0];
print("enter the entering time by hour & minute separated with a space.")
inlet1=input()
inlet2=list(map(int,inlet1.split(' ')))
if len(inlet2)!=2:
    print("pedarsag!")

