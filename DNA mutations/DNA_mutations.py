def main():
    file_name=input("Enter the file name : ")
    file=open(file_name)
    content=file.read()
    l1=content.split('\n')
    l2=[]
    for i in l1:
        l3=[]
        for j in i:
            l3.append(j)
        l2.append(l3)
    return l2
#[['A', 'C', 'C', 'G', 'T', 'G', 'A', 'A', 'T', 'T'], ['A', 'G', 'G', '_', 'A', 'G', 'A', 'A', 'T', 'T']]
lst=main()
def mutation_score(l):
    parent=l[0]
    child=l[1]
    score=0
    for i in range(len(parent)):
        if parent[i]==child[i]:
            score+=0
        elif child[i]=='_':
            score+=6
        elif (parent[i]=='A' and child[i]=='T') or (parent[i]=='T' and child[i]=='A'):
            score+=2
        elif (parent[i]=='G' and child[i]=='C') or (parent[i]=='C' and child[i]=='G'):
            score+=2
        else:
            score+=4

    print(score)

mutation_score(lst)