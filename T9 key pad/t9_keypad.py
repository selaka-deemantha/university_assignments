def main():
    file_name = input("Enter the file name : ")
    file = open(file_name)
    content = file.read()
    lst = [i for i in content]
    return lst


def checker(a, b):
    if abs(ord(a) - ord(b)) == 0:
        return True
    if abs(ord(a) - ord(b)) == 1:
        if ord(a) > ord(b):
            if a != 'd' and a != 'g' and a != 'j' and a != 'm' and a != 'p' and a != 't' and a != 'w':
                return True
            else:
                return False
        else:
            if b != 'd' and b != 'g' and b != 'j' and b != 'm' and b != 'p' and b != 't' and b != 'w':
                return True
            else:
                return False
    else:
        return False


def func(lst):
    ans = []
    a = ""
    for i in range(len(lst) - 1):
        if checker(lst[i], lst[i + 1]):
            a += lst[i]
            if i == len(lst) - 2:
                a += lst[i + 1]
                ans.append(a)
                a=""
        else:
            if len(a) == 0:
                ans.append(lst[i])
                if i == len(lst) - 2:
                    ans.append(lst[i + 1])
            else:
                a += lst[i]
                ans.append(a)
                a = ""
                if i == len(lst) - 2:
                    ans.append(lst[i + 1])
    return ans


s = "you know nothing."
lst = [i for i in s]
ll = func(lst)
w = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz', ' ', '.']

tt=0
for i in range(len(ll)):
    if len(ll[i])==1:
        idx=0
        for j in w:
            if ll[i] in j:
                idx =j.index(ll[i])+1
        tt += (0.2*idx)
        tt+=0.4
    else:
        for f in range(len(ll[i])):
            idx=0
            for j in w:
                if ll[i][f] in j:
                    idx = j.index(ll[i][f]) + 1
            tt += (0.2 * idx)
            if f==len(ll[i])-1:
                tt+=0.4
            else:
                tt+=0.7
tt-=0.4
print(tt)





