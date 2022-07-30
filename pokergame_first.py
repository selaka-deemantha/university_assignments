def pokerpalyer(s):
    l = s.split()
    pl1 = l[:5]
    pl2 = l[5:]

    return pl1, pl2


def fun(l):
    suit = [i[1] for i in l]
    value = [i[0] for i in l]
    for j in range(5):
        if value[j] == 'T':
            value[j] = 10
        if value[j] == 'J':
            value[j] = 11
        if value[j] == 'Q':
            value[j] = 12
        if value[j] == 'K':
            value[j] = 13
        if value[j] == 'A':
            value[j] = 14
    value = [int(i) for i in value]

    # check rank 6
    r = [10, 11, 12, 13, 14]
    if sorted(r) == sorted(value) and len(set(suit)) == 1:
        return 6

    # check rank 5 or 3
    if len(set(suit)) == 1:
        h = True
        min_val = min(value)
        for i in range(4):
            min_val += 1
            if min_val not in value:
                h = False
        if h:
            return 5
        else:
            return 3

    # check rank 2 or 4
    k = False
    l1 = sorted(value)
    for i in range(3):
        if l1[i] == l1[i + 1] and l1[i + 1] == l1[i + 2] and l1[i] == l1[i + 2]:
            k = True
            v = l1[i]

    if k:
        nv = [i for i in value if i != v]
        if len(set(nv)) == 1:
            return 4
        else:
            return 2

    else:
        return 1


lst1, lst2 = pokerpalyer('5D 8C 9S JS AC 3D 6D 7D TD QD')
print(lst1, lst2)
print(fun(lst2))