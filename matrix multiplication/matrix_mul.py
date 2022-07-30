def matrix_mul(s1,m1,s2,m2):
    if s1[1]!=s2[0]:
        return "Invalid input"
    else:
        ans=[]
        for i in range(s1[0]):
            ans.append([])


def helper_func1(l1,l2):
    ans=0
    for i in range(len(l1)):
        ans+=(l1[i]*l2[i])
    return ans
def helper_func2(l):
    ans=[]
    for i in range(len(l)):
        for j in range(len(l[0])):


print(helper_func2([[1,2,3],[4,5,6]]))