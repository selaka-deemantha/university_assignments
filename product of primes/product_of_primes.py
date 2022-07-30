

def prime_checker(n):
    l = [i for i in range(2, n) if n % i == 0]
    if len(l) == 0:
        return True
    else:
        return False


def prime_list(n):
    if n == 1:
        return None
    ans = []
    while True:
        dev = True
        i = 1
        while dev:
            i += 1
            if n % i == 0 and prime_checker(i):
                dev = False

        ans.append(i)
        n = int(n / i)
        if n == 1:
            break
    return ans


def prime_factor_display(l):
    ans = []
    while len(l) > 0:
        min = l[0]
        for i in range(len(l)):
            if l[i] < min:
                min = l[i]
        ans.append(min)
        l.remove(min)
    #print(ans)

    ans1 = []
    ans2=[]
    for i in ans:
        if i not in ans1:
            ans1.append(i)
    for i in ans1:
        k = 0
        for j in ans:
            if i == j:
                k += 1
        ans2.append(k)
    ans3=""
    for i in range(len(ans1)):
        if ans2[i]>1:
            ans3+=(str(ans1[i])+"^"+str(ans2[i])+" X ")
        else:
            ans3 += (str(ans1[i]) + " X ")
    print(ans3[:-2])



prime_factor_display(prime_list(68456))

