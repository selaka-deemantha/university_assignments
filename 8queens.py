def diagonal_checker(q1, q2):
    if abs(ord(q1[0]) - ord(q2[0])) == abs(int(q1[1]) - int(q2[1])):
        return False
    else:
        return True


# print(diagonal_checker('c4','b7'))
def vertical_and_horizontal_checker(s):
    lst1 = s.split()
    ansc = []
    ansr = []
    col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    row = ['1', '2', '3', '4', '5', '6', '7', '8']
    pcol = [i[0] for i in lst1]
    prow = [i[1] for i in lst1]
    for i in range(8):
        if col[i] not in pcol:
            ansc.append(col[i])
        if row[i] not in prow:
            ansr.append(row[i])
    ans = [i + j for i in ansc for j in ansr]
    return ans
locations='a1 b3 d6 f2 g4 h7'
ans=[]
for i in vertical_and_horizontal_checker(locations):
    result=True
    for j in locations.split():
        if not diagonal_checker(i, j):
            result=False
    if result:
        ans.append(i)

print(ans)

