def mean(l):
    sum_=0
    for i in l:
        sum_+=i
    return round(sum_/len(l),2)

def mode(l):
    max_=0
    u=[]
    ans=[]
    set_=[]
    for i in l:
        if i not in set_:
            set_.append(i)
    for i in set_:
        count=0
        for j in l:
            if i==j:
                count+=1
        if max_<count:
            max_=count
        u.append([str(i),count])
    for i in u:
        if i[1]==max_:
            ans.append(i[0])

    return ans



def range(l):
    max_=0
    min_=l[0]
    for i in l:
        if max_<i:
            max_=i
        if min_>i:
            min_=i
    return max_-min_

def median(l):
    d=True
    k=False
    i=0
    while d:
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            k=True
        if i==len(l)-2:
            i=0
            if k:
                k=False
            else:
                d=False
        else:
            i+=1

    if len(l)%2==0:
        n=len(l)//2
        med=(l[n]+l[n-1])/2
    else:
        n=(len(l)-1)//2
        med=l[n]
    return int(med)


def main(l):
    print("mean : ",mean(l))
    print("median : ",median(l))
    print("mode : ",",".join(mode(l)))
    print("range : ",range(l))
main([13,18,13,14,13,16,14,21,13,14,14,5,5,5,5])
