"""
def func(l,n):
    r=0
    k=1
    for i in range(1,len(l)+1):
        k*=i
    p=k//len(l)
    l=sorted(l)
    s=n//p
    m=n%p
    if m==0:
        s-=1
    if n<=p:
        r=n
    else:
        r=m

    return l[s],r


#print(func([2],1))


def fun1(ls,n):
    ll = []
    l=[i for i in ls]
    for i in range(4):
        if l == []:
            break
        a,n = func(l, n)
        ll.append(a)
        l.remove(a)

    print(ll)
def g(lst,num):
    gg=1
    for i in range(1,len(lst)+1):
        gg*=i
    fun1(lst, 1)
    fun1(lst,num)
    fun1(lst, gg)



g([0,1,2,3],12)
"""
permutations=[]
def perm(num,list1):

    #When the list1 is empty, num has reached it's full length
    if len(list1)==0:
        permutations.append(num)

    #elements of the list1 are being added to num
    for NUM in list1:
        index = list1.index(NUM)
        perm(num+NUM,list1[:index]+list1[index+1:]) #NUM is removed from list1 to prevent infinity loops
                                                    #and to prevent same digit being in num twice

#Generate the permutations
perm("",['0','1','2','3'])
print(permutations)
