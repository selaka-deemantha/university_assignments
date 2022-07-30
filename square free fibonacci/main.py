def fib_gen(n):
    a=0
    b=1
    count=2
    while count<=n:
        a,b=b,a+b
        count+=1
    return b

def prime_checker(n):
    if n==0 or n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def squ_prime(n):
    if n**(1/2)==int(n**(1/2)) and prime_checker(int(n**(1/2))):
        return True
    else:
        return False



def prime_squ_checker(n):
    num=fib_gen(n)
    for i in range(2,num+1):
        if num%i==0:
            if squ_prime(i):
                return "NO"
    return "YES"

print(prime_squ_checker(4))
