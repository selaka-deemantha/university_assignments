def main():
    file_name=input('Enter the file name :')
    file=open(file_name)
    lst=file.read().split('\n')
    ans=[]
    for i in lst[1:]:
        ans.append(list(map(int,i.split())))
    return int(lst[0]),ans

a,b=main()
#print(a)

def transpose(m):
    ans=[]
    for i in range(len(m)):
        l1=[]
        for j in range(len(m)):
            l1.append(m[j][i])
        ans.append(l1)
    return ans



def horizontal_maximum(l):
    ans=[]
    for i in l:
        sum_=0
        for j in range(len(i)-2):
            sum_=(i[j]+i[j+1]+i[j+2])
            ans.append(sum_)
    return max(ans)

def vertical_maximum(l):
    return horizontal_maximum(transpose(l))


print(horizontal_maximum(b),vertical_maximum(b))

#print(transpose([[1,2,3],[4,5,6],[7,8,9]]))



