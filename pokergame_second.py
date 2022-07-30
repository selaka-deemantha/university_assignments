def player_divider(s):
    l = s.split()
    tot_suit = [i[1] for i in l]
    value = [i[0] for i in l]
    for j in range(10):

        if value[j].isnumeric():
            value[j] = int(value[j])

        elif value[j] == 'T':
            value[j] = 10
        elif value[j] == 'J':
            value[j] = 11
        elif value[j] == 'Q':
            value[j] = 12
        elif value[j] == 'K':
            value[j] = 13
        elif value[j] == 'A':
            value[j] = 14

    return [value[:5], tot_suit[:5]], [value[5:], tot_suit[5:]]


def unique_checker(l):
    ans = []
    l1 = sorted(set(l))
    for i in l1:
        ans.append(l.count(i))
    return ans


def consecutive_checker(l):
    ans = True
    min_val = min(l)
    for i in range(len(l) - 1):
        min_val += 1
        if min_val not in l:
            ans = False
    return ans

def poker_game(pl_v,pl_s):
    if unique_checker(pl_s)==[5]:
        if sorted(pl_v)==[10,11,12,13,14]:
            return 6
        elif consecutive_checker(pl_v):
            return 5
        else:
            return 3
    a=unique_checker(pl_v)
    if 3 in a:
        if sorted(a)==[2,3]:
            return 4
        else:
            return 2
    else:
        return 1

pl1,pl2=player_divider('3D 6D 7D TD QD 2H 2D 4C 4D 4S')
print(pl1)
print(poker_game(pl1[0],pl1[1]))
print(pl2)
print(poker_game(pl2[0],pl2[1]))
