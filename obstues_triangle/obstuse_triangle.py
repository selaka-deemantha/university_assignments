def distance(l):
    l1=(((l[0][0]-l[1][0])**2)+((l[0][1]-l[1][1])**2))
    l2=(((l[0][0]-l[2][0])**2)+((l[0][1]-l[2][1])**2))
    l3=(((l[1][0]-l[2][0])**2)+((l[1][1]-l[2][1])**2))
    if l1>l2+l3 or l2>l1+l3 or l3>l1+l2:
        return True
    else:
        return False

def main(lst):
    count=0
    h=0
    length=len(lst)
    for i in range(length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                h+=1
                arr=[lst[i],lst[j],lst[k]]

                if distance(arr):
                    count+=1

    print(count)

main([[2,3],[0,2],[1,1],[3,5]])