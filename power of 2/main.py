def is_power_of_2(n):
    while n!=1:
        if n%2!=0:
            return False
        n=n//2
    return True
def main(l):
    ans=0
    for i in l:
        if is_power_of_2(i):
            ans+=1
    return ans

