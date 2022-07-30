def main():
    file_name=input('Enter the file name :')
    file=open(file_name)
    lst=file.read().split('\n')
    ans=[]
    number_of_input=int(lst[0])
    for i in lst[1:]:
        ans.append(i.split())
    return number_of_input,ans

a,b=main()
#print(a,b)

def string_shoter(s):
    if len(set(s)) == 1:
        return s[0]
    else:
        if s[0] != s[1]:
            return s[0] + string_shoter(s[1:])
        else:
            i = 0
            while s[i] == s[i + 1]:
                i += 1
            return s[0] + string_shoter(s[i+1:])

for i in b:
    short_s=string_shoter(i[0])
    print(short_s)
    try:
        print(short_s[int(i[1])-1])
    except:
        print('position out of range')