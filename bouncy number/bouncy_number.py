def bouncy_checker(n):
    if n<100:
        return False
    l=[int(i) for i in str(n)]
    a=0
    b=0
    for i in range(len(l)-1):
        if l[i]<=l[i+1]:
            a+=1
    for j in range(len(l)-1):
        if l[j]>=l[j+1]:
            b+=1
    if a==len(l)-1 :
        return False
    if b==len(l)-1 :
        return False
    else:
        return True


def main(p, q):
    tot = 0
    for i in range(p, q + 1):
        if bouncy_checker(i):
            tot += i

    print(tot)
main(100,1000)
