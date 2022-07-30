def collatz_series(n):
    max_=n
    k=0
    while n>1:
        if n%2==0:
            n/=2
        else:
            n=3*n+1
            if max_<n:
                max_=n
        k+=1
    return k,int(max_)
#print(collatz_series(3))

def main(n1,n2):
    max_v=0
    t_s_t=0
    for i in range(n1+1,n2):
        if max_v<collatz_series(i)[1]:
            max_v=collatz_series(i)[1]
        if t_s_t<collatz_series(i)[0]:
            t_s_t=collatz_series(i)[0]
    print(t_s_t,max_v)

main(700,1000)

