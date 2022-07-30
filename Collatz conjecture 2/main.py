
def func(n):
    tot_stp_tim=0
    max_=n
    while n!=1:
        tot_stp_tim+=1
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        if max_<= n:
            max_=n
    return max_,tot_stp_tim

def main(n1,n2):
    m=0
    t=0
    state=True
    for i in range(n1+1,n2):
        a1,a2=func(i)
        if state:
            m,t=func(i)
            state=False
        if m<a1:
            m=a1
        if t<a2:
            t=a2
    return t,m

print(main(700,1000))

