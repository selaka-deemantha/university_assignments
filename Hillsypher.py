def string_to_matrix(s):
    k = 0
    lst = []
    s=s.lower()
    if len(s) % 3 == 1:
        s += '  '
    if len(s) % 3 == 2:
        s += ' '
    for i in range(len(s) // 3):
        lst1 = []
        for j in range(3):
            if s[k + j].isalpha():
                lst1.append(ord(s[k + j]) - 97)
            else:
                lst1.append(26)
        lst.append(lst1)
        k += 3

    return lst


# print(string_to_matrix('abcdefgh'))
def matrix_mul(n):
    m = [[3, 8, 12], [23, 4, 1], [21, 19, 5]]
    ans = []
    for i in m:
        l = 0
        sum_ = 0
        for j in i:
            p=j * n[l]
            sum_ += p
            l += 1
        ans.append(sum_ % 27)

    return ans


# print(matrix_mul([[2],[0],[17]]))
def matrix_to_string(m):
    b=list('abcdefghijklmnopqrstuvwxyz ')
    st=''
    for i in m:
        st+=b[i]
    return st


#print(matrix_to_string([1,26,24]))

def endcoder(s):
    ans=''
    l1=string_to_matrix(s)
    for i in l1:
        ans+=matrix_to_string(matrix_mul(i)).upper()
    return ans

print(endcoder("AB"))


