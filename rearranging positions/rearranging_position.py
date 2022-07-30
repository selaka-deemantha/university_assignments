def swapping(s, l, idx):
    swap_directon = s[0]
    number_of_swapps = int(s[1])
    if swap_directon == "R":
        for i in range(number_of_swapps):
            l[idx],l[idx+1]=l[idx+1],l[idx]
            idx+=1
        return l
    if swap_directon=="L":
        for i in range(number_of_swapps):
            l[idx],l[idx-1]=l[idx-1],l[idx]
            idx-=1
        return l
#print(swapping("L2",["a","b","c","d","e","f"],2))
def main(s1,s2):
    ans=""
    student_line=s1.split(" ")
    line=[i for i in student_line]
    instructions=s2.split(" ")
    k=0
    for i in instructions:
        student_line=swapping(i,student_line,student_line.index(line[k]))
        k+=1
    for i in line:
        ans+=str(student_line.index(i)+1)
        ans+=" "
    print(ans)


main("A B C D E","R1 R2 L1 R1 L3")

