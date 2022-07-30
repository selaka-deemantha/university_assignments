def fun(l):
    temp=[]
    dup=[]
    idx=[]
    for i in l:
        if i not in temp:
            temp.append(i)
        else:
            dup.append(i)
    for i in range(len(l)):
        if l[i] in dup:
            idx.append(i+1)
    if len(idx)==0:
        print("None")
    else:
        print(sorted(idx))

fun([1,3,5,7,8,90,7,56,33,90])

