def fibonacii_generator(n):
    if n==0:
        return 0
    a=0
    b=1
    for i in range(n-1):
        a,b=b,a+b
    return b
def factors(n):
    for i in range(1,n+1):
        if i==1:
            continue
        if n%i==0:
            if i**(1/2)==int(i**(1/2)):
                print(i)
                return True
    return False
def f(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    print(l)

print(factors(fibonacii_generator(16)))
f(fibonacii_generator(16))