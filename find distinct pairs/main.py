def fun(n,k):
    ans=0
    for i in range(n+1):
        if i>k/2:
            break
        for j in range(i+1,n+1):
            if i+j>k:
                break
            if i+j==k:
                ans+=1
    print(ans)
fun(20,23)

