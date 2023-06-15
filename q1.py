i=3
while (i!=2):
    while (i!=2):
        print("enter the entering time in hour & minute separated with a space.")
        in1=input()
        in2=list(map(int,in1.split(' ')))
        i=len(in2)
        if i!=2 or in2[0]>22 or in2[0]<6 or in2[1]>59 or in2[1]<0:
            print("invalid data.\nStartover")
            i=5
            break
        else:
            time1=in2[0]*60+in2[1]
            j=3
            while (j!=2):
                while (j!=2):
                    print("enter the leaving time in hour & minute separated with a space.")
                    in1=input()
                    in2=list(map(int,in1.split(' ')))
                    j=len(in2)
                    time2=in2[0]*60+in2[1]
                    if j!=2 or in2[0]>22 or in2[0]<6 or in2[1]>59 or in2[1]<0 or time1>time2:
                        print("invalid data.\nStartover")
                        j=5
                        break
                    break
        break
b=int((time2-time1)/60)
print(b)
