i=3
while(i!=2):
    while (i!=2):
        print("enter the entering time in hour & minute separated with a space.")
        in1=input()
        in2=list(map(int,in1.split(' ')))
        i=len(in2)
        if i!=2 or in2[0]>22 or in2[0]<6:
            print("enter 2 numbers.")
            i=5
            break
        else:
           print("hi")
        break
