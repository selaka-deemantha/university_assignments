def fun(s):
    l={}
    i=0
    m=0
    while i<len(s):
        if s[i] not in l:
            l[s[i]]=i
            #print(l)
            i+=1
            if m<len(l):
                m=len(l)
        else:
            i=i-(len(l)-l.index(s[i])-1)
            #print(s[i])
            l=[]
    print(m)




fun("dvjagthdf")