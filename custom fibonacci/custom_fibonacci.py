def fun(n):
    if n==2:
        return 15
    if n==1:
        return 4
    if n==0:
        return 0
    else:
        return (((3*(n+3))/(n+2))*fun(n-1))-(((2*(n+3))/(n+1))*fun(n-2))


print(fun(12))