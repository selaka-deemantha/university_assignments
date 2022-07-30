def binary_conv(n):
    ans=""
    while(n!=1):
        ans=str(n%2)+ans
        n=n//2
    else:
        ans=str(1)+ans
    return int(ans)

def palindromic_checker(n):
    length=len(str(n))
    for i in range(length//2):
        if str(n)[i]!=str(n)[length-1-i]:
            return False
    return True

def main():
    while True:
        num=int(input("ENTER THE NUMBER : "))
        if num==-1:
            break
        else:
            if palindromic_checker(num) and palindromic_checker(binary_conv(num)):
                print("YES")
            else:
                print("NO")

main()