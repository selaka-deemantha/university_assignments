def look_and_say(n,s):
    k=str(1)+s
    l=[s,k]
    f=True
    q=0
    while f:
        a=[]
        ite=0
        b=False
        for i in range(len(k)):
            if i == len(k) - 1:
                if b:
                    ite+=1
                    a.append(str(ite))
                    a.append(k[i])
                    continue
                else:
                    a.append(str(1))
                    a.append(k[i])

            if i<len(k)-1:
                if k[i]==k[i+1]:
                    ite+=1
                    b=True
                    continue


                else:
                    if b:
                        ite+=1
                        a.append(str(ite))
                        a.append(k[i])
                        b=False
                        ite=0
                    else:
                        a.append(str(1))
                        a.append(k[i])


        k="".join(a)
        l.append(k)
        q+=1
        if len(l)==n:
            f=False
    print(l)

look_and_say(4,"6")