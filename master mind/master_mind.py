def score_checker(a,b):
    a1=[i for i in a]
    b1=[i for i in b]
    hits=0
    p_hits=0
    k=0
    m=0
    while k!=4:
        k+=1
        if a1[m]==b1[m]:
            hits+=1
            a1.remove(a1[m])
            b1.remove(b1[m])
        else:
            m+=1
    for i in a1:
        if i in b1:
            p_hits+=1
    return (hits,p_hits)
l=['gyrr','bbrr','gryr','gryb']
for i in l:
    print(score_checker(i,"rrgy"))