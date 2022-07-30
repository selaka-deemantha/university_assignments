def sorted_list(msg):
    l1 = []
    for i in msg:
        if i not in l1 and i != " ":
            l1.append(i)
    ans=[]
    for i in range(ord('A'),ord('Z')+1):
        if chr(i) in l1:
            ans.append(chr(i))
    return ans
def encoder(s,l):
    for i in range(len(l)):
        if l[i]==s:
            a=len(l)-1-i
            return l[a]
def main(s):
    lst=sorted_list(s)
    ans=""
    for i in s:
        if i ==" ":
            ans+=i
            continue
        ans+=encoder(i,lst)
    print(ans)
main("MEET ME AT HOGSMEADE TODAY")






sorted_list("CBADEZXW")