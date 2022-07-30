def min_(x, lst):
    l = []
    for i in lst:
        l.append(min(x,i))
    return l

def graphic_sequence(l):
    sum_ = sum(l)
    n = len(l)
    a=True
    for i in range(1, n + 1):
        if sum(l[:i])<=(i*(i-1) + sum(min_(i,l[i+1:]))) and sum_%2==0:
            continue
        else:
            n=False
            break
    if n:
        print("Graphic")
    else:
        print("Non-Graphic")

graphic_sequence([12,2,1,1])