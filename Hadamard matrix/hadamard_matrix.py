def mat_mul(mat1,mat2,n):
    ans=[]
    for i in range(n):
        l=[]
        for j in range(n):
            tot=0
            for k in range(n):
                tot+=mat1[i][k]*mat2[k][j]
            l.append(tot)
        ans.append(l)
    return ans
def identity_matrix_checker(mat):
    n=len(mat)
    num=0
    for i in range(n):
        for j in range(n):
            if j==i:
                if mat[i][i]==0:
                    return False
                else:
                    if num==0:
                        num=mat[i][i]
                    else:
                        if mat[i][i]!=num:
                            return False
            else:
                if mat[i][j]!=0:
                    return False
    return True

def transpose(mat):
    l=[]
    n=len(mat)
    for i in range(n):
        k=[]
        for j in range(n):
            k.append(mat[j][i])
        l.append(k)
    return l
def hadmard_matrix_checker(mat,n):
    ans=mat_mul(mat,transpose(mat),n)
    if identity_matrix_checker(ans):
        return "Harmard"
    else:
        return "Not Harmard"




print(hadmard_matrix_checker([[2,-1],[-1,-1]],2))
