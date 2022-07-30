def fun(n):
    i=1
    k=1
    sum_=0
    ans=None
    p=""
    while True:
        sum_=i
        p=str(i)
        for j in range(n-1):
            i+=2
            sum_+=i
            p+=" + "+str(i)
        if sum_==n*n*n:
            print("Odd number sequence : ",p)
            ans=k
            break
        else:
            k+=2
            i=k

def fun2(n):
    i=1
    sum_=0
    while True:
        sum_=n*(i+(n-1))
        if sum_==n*n*n:
            break
        else:
            i+=2
    ans="Odd Number Sequence : "+str(i)
    for j in range(n-1):
        i += 2
        ans+=" + "+str(i)

    print(ans)

input_=None
while True:
    input_=input("Enter input : ")
    if input_=="-1":
        print("Bye!")
        break
    if not (1<=int(input_) and int(input_)<=20):
        print("n should be within [1,20]")
        continue

    else:
        fun2(int(input_))

