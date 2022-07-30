def IS_NOT_SHUFFLE(s1,s2):
    if s1=="" or s2=="":
        return False
    k=0
    i=0
    while True:
        if i+k==len(s2):
            return False
        if s1[k]==s2[i+k]:
            k+=1
            if k==len(s1):
                return True
        else:
            k=0
            i+=1
print(IS_NOT_SHUFFLE("o","hello"))

def IS_SHUFFLE(s1,s2):
    if s1=="" or s2=="":
        return False
    for i in s1:
        if i not in s2:
            return False
    return True
def main(word1,word2,word3):
    if IS_NOT_SHUFFLE(word1,word3) and IS_NOT_SHUFFLE(word2,word3):
        return "NOT A SHUFFLE"
    elif IS_SHUFFLE(word1,word3) and IS_SHUFFLE(word2,word3):
        return "SHUFFLE"
    else:
        return "THIRD WORD DOES NOT CONTAIN FIRST TWO WORDS"
print(main("o","what","hihellogowhta"))

def fun(str1,str2):
    temp=str2
    for i in str1:
        if i==temp[0]:
            temp=temp[1:]
            print(temp)
            if temp=="":
                return True
        else:
            temp=str2

    return False

print(fun("eghelloh","hellogg"))