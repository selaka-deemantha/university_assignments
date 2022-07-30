def fib_generator(n):
    fib_series=[]
    k=1
    l=2
    for i in range(n):
        if i==0:
            fib_series.append(1)
            continue
        if i==1:
            fib_series.append(1)
            continue
        fib_series.append(l)
        k,l=l,k+l
    return fib_series[-1]

def distance_finder(t):
    dis=0
    for i in range(1,t+1):
        dis+=((fib_generator(i))**(1/2))
    dis=round(dis,3)
    print(dis)

distance_finder(2)

