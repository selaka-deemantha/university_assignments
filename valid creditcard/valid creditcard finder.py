'''
def main():
    filename=input('Enter the file name : ')
    file=open(filename)
    content=file.read()
    lst=content.split('\n')
    num=int(lst[0])
    ans=lst[1:]
    return num,ans

num,card_numbers=main()
'''

def valid_hyphen(s):
    lst=s.split('-')
    for i in lst:
        k=0
        for j in i:
            if not j.isnumeric():
                return False
            k+=1
        if k!=4:
            return False
    return True

#print(valid_hyphen('1200-5637-9113'))

def repeted_digits_checker(s):
    for i in range(len(s)-3):
        if s[i]==s[i+1] and s[i+1]==s[i+2] and s[i+2]==s[i+3]:
            return False
    return True
#print(repeted_digits_checker('1113222411145555'))

def checker(s):
    number=''
    v='valid'
    iv='invalid'
    for i in s:
        if i.isnumeric() or i=='-':
            continue
        return iv
    if '-' in s:
        if  valid_hyphen(s):
            l=s.split('-')
            for i in l:
                number+=i
        else:
            return iv
    else:
        number=s
    if repeted_digits_checker(number):
        if len(number)==16 and (number[0]=='4' or number[0]=='5' or number[0]=='6'):
            return v
        else:
            return iv
    else:
        return iv



print(checker('4123-3567-8912-3456'))
#a=valid_hyphen('1234-1234-1234')
#print(a)