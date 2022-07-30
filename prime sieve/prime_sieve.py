"""
def prime_sieve(l,k=0):
    new_l=[i for i in l if i==l[k] or i%l[k]!=0]
    if len(l)==len(new_l):
        return new_l
    else:
        return prime_sieve(new_l,k=k+1)

def main(n):
    l=[i for i in range(2,n+1)]
    return prime_sieve(l)

print(main(10))
"""


def prime_sieve(n):
    l = [i for i in range(1, n + 1)]
    l.remove(1)
    for i in l:
        temp_list = [j for j in l if j != i]
        for j in temp_list:
            if j%i==0:
                l.remove(j)

    print(l)
prime_sieve(15)


