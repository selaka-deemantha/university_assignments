def gcd(a,b):
    while b!=0:
        t=b
        b=a%b
        a=t
    return a

def lcm(a,b):
    return (a*b)/gcd(a,b)


file=open('sof.txt')
a=file.read().split()
file.close()
#print(a)
denomi=1
nume=0
for i in range(int(a[0])):
    denomi*=int(a[i+1].split('/')[-1])
#print(denomi)
for i in range(int(a[0])):
    nume+=((denomi/int(a[i+1].split('/')[-1]))*int(a[i+1].split('/')[0]))
#print(nume)
if gcd(denomi,nume)==denomi:
    print(int(nume/denomi))
else:
    if gcd(denomi,nume)!=1:
        while gcd(denomi,nume)!=1:
            d=gcd(denomi,nume)
            denomi=int(denomi/d)
            nume=int(nume/d)
        else:
            print(str(nume)+'/'+str(denomi))
    else:
        print(str(nume)+'/'+str(denomi))

