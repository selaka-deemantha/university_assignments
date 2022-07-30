def height(lst):
    ans=0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]==lst[j] and lst[i]!="XX":
                ans+=1
                lst[j]="XX"
                break
    return ans

def simplyfied_fun(lst):
    ans=0
    k=0
    for i in lst:
        if lst.count(i)>1:
            if lst.count(i)%2==0:
                ans+=(1/2)
            else:
                ans+=(1/2)
                k+=(1/2)/lst.count(i)

    print(int(ans-k))
simplyfied_fun([1,2,3,3,4,4,5,6,5,5,5,2,2])
print(height([1,2,3,3,4,4,5,6,5,5,5,2,2]))

lst=input("Enter the heights : ").strip().split()
state=True
for i in lst:
    if not i.isnumeric():
        print("there is not numeric value in your input")
        state=False
        break
    if int(i)<100 or int(i)>200:
        print("height must be in [100,200]")
        state=False
        break
if state:
    lst=map(int, lst)
    print("Number of dancing pairs : ",height(list(lst)))