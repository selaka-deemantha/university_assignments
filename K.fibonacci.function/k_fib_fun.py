#typical way
def fun(k,n):
    nn=1
    lst=[]
    while True:

        if nn<=k:
            lst.append(1)
        else:
            a=sum(lst[-k:])
            lst.append(a)
        if nn==n:
            break
        nn+=1
    print(lst[-1])

fun(13,39)






