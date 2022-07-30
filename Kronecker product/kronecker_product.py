

def fun(n,a,b):
    mat=[]
    for i in range(n):
        l1=a[i]
        for j in range(n):
            l2=b[j]
            row=[]
            for k in l1:
                for h in l2:
                    row.append(k*h)
            mat.append(row)
    print(mat)

fun(2,[[1,2],[5,6]],[[0,0],[1,-1]])



