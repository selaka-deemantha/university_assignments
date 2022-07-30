def is_prime(n):
    if n == 1 or n == 0:
        return False
    l = [i for i in range(2, n) if n % i == 0]
    if len(l) == 0:
        return True
    else:
        return False


def prime_factor_finder(n):
    ans=[]
    i=1
    while n>1:
        if n%i==0 and is_prime(i):
            ans.append(i)
            n =int(n/i)
            i=1
        i+=1
    return ans
def is_humming_number(l):
    l=set(l)
    for i in l:
        if i==2 or i==3 or i==5:
            continue
        return False
    return True
def main(p,q):
    tot=0
    for i in range(p,q+1):
        if is_humming_number(prime_factor_finder(i)):
            tot+=i

    print(tot)

main(10,20)




