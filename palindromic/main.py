def palindromic_checker(num):
    for i in range(len(str(num))//2):
        if str(num)[i]!=str(num)[len(str(num))-1-i]:
            return False
    return True

def rev_generator(num):
    ans=""
    for i in range(len(str(num))):
        ans+=str(num)[len(str(num))-1-i]
    return int(ans)

def main(n):
    if palindromic_checker(n):
        return n
    else:
        k=0
        while k<=25:
            k += 1
            n=n+rev_generator(n)
            if palindromic_checker(n):
                return n


        return "Too long"
print(main(13))
