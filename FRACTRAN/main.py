def main(n):
    l=[[455,33],[11,13],[1,11],[3,7],[11,2],[1,3]]
    i=0
    count=0
    while True:
        if i==6:
            return count,int(n)
        if n*l[i][0]%l[i][1]==0:
            n=n*l[i][0]/l[i][1]
            count+=1
            i=0
        else:
            i+=1

print(main(6))