def main():
    file_name=input('Enter the file name')
    file=open(file_name)
    content=file.read()
    lst=content.split('\n')
    return lst

def digital_list(s):
    ans=[]
    for i in s:
        if int(i)==0:
            ans.append(['+-+', '| |', '   ', '| |', '+-+'])
        if int(i)==1:
            ans.append(['   ', '  |', '   ', '  |', '   '])
        if int(i)==2:
            ans.append(['+-+', '  |', '+-+', '|  ', '+-+'])
        if int(i)==3:
            ans.append(['+-+', '  |', '+-+', '  |', '+-+'])
        if int(i)==4:
            ans.append(['   ', '| |', '+-+', '  |', '   '])
        if int(i)==5:
            ans.append(['+-+', '|  ', '+-+', '  |', '+-+'])
        if int(i)==6:
            ans.append(['+-+', '|  ', '+-+', '| |', '+-+'])
        if int(i)==7:
            ans.append(['+-+', '  |', '   ', '  |', '   '])
        if int(i)==8:
            ans.append(['+-+', '| |', '+-+', '| |', '+-+'])
        if int(i)==9:
            ans.append(['+-+', '| |', '+-+', '  |', '+-+'])
    return ans
def digital_show(l):
    for i in range(5):
        x=''
        for j in range(len(l)):
            x+=l[j][i]+' '
        print(x)

lst=main()
for i in lst:
    digital_show(digital_list(i))



