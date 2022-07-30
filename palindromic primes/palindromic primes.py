def is_palindromic(n):
    l = [i for i in str(n)]
    for i in range(len(l) // 2):
        if l[i] != l[-(i + 1)]:
            return False
    return True


def is_prime(n):
    if n == 1 or n == 0:
        return False
    l = [i for i in range(2, n) if n % i == 0]
    if len(l) == 0:
        return True
    else:
        return False


def is_square(n):
    n1 = n ** (1 / 2)
    b = str(n1)
    l = b.split(".")
    if int(l[1]) == 0:
        return True
    else:
        return False


def main(a, b):
    ans = 0
    for i in range(a, b):
        if is_prime(i) and is_palindromic(i):
            ans += i
        if is_palindromic(i) and is_square(i):
            ans += i
    print(ans)


main(0, 10)
