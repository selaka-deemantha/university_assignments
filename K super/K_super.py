def list_generator(m, n):
    ans=[]
    l=[str(m)]
    for i in str(n):
        l.append(i)
    ans.append(int("".join(l)))
    for i in range(len(str(n))):
        a=l[i]
        b=l[i+1]
        l[i],l[i+1]=b,a
        ans.append(int("".join(l)))
    return ans

def k_super_checker(k,m,n):
    l=[i for i in list_generator(m,n) if i%(2**k)!=0]
    if len(l)>0:
        return False
    else:
        return True

print(k_super_checker(3,0,43406193657965875880))
