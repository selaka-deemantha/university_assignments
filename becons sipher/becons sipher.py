def binary_converter(num):
    if num==0:
        return 0
    if num==1:
        return 1
    else:
        return 10*binary_converter(num//2) + num%2

def encryptor(s):
    ans=''
    ans1=''
    l=s.split()
    for i in l:
        for j in i:
            a=binary_converter(ord(j.lower())-ord('a'))
            ans+='0'*(5-len(str(a)))+str(a)
    for i in ans:
        if i=='0':
            ans1+='A'
        else:
            ans1+='B'
    print(ans1)
encryptor('hello world')
