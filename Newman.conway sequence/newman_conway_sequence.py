#first recurtion function isn't work because maximum recursion depth is exceeding
def newman_conway_seq(n):
    if n<=2:
        return 1
    else:
        return newman_conway_seq(newman_conway_seq(n-1)) + newman_conway_seq(n-newman_conway_seq(n-1))

def fun(n):
    l={"p1":1,"p2":1}
    k=3
    while k<=n:
        t="p"+str(k)
        l[t]=l.get("p"+str(l.get("p"+str(k-1)))) + l.get("p"+str(k-l.get("p"+str(k-1))))
        k+=1
    print(l.get("p"+str(n)))

fun(15264)
