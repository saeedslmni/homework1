i=3
while (i!=2):
    while (i!=2):

        print("enter the entering time in hour & minute separated with a space.")
        in1=input()
        in2=list(map(int,in1.split(' ')))
        i=len(in2)
        if i!=2 or in2[0]>22 or in2[0]<6 or in2[1]>59 or in2[1]<0:
            print("invalid data.\n Startover")
            i=5
            break
        else:
           print("hi")
        break
