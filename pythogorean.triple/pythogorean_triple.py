def primitive_checker(l):
    a=l[0]
    b=l[1]
    c=l[2]
    if a**2 + b**2!=c**2:
        return False
    if c%2==0:
        for i in range(2,c//2):
            if a%i==0 and b%i==0 and c%i==0:
                return False
        return True
    else:
        for i in range(2,(c+1)//2):
            if a % i == 0 and b % i == 0 and c % i == 0:
                return False
        return True

def pythogorean_triple_generator(n):
    ans=[]
    for i in range(1,n):
        for j in range(i+1,n):
            if (i*i + j*j)**(1/2)==int((i*i + j*j)**(1/2)) and (i*i + j*j)**(1/2)<n:
                ans.append([i,j,int((i*i + j*j)**(1/2))])
    return ans


def main(n):
    count=0
    ans=pythogorean_triple_generator(n)
    for i in ans:
        if primitive_checker(i):
            count+=1

    return count

print(main(1000))
