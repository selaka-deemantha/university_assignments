def main():
    file_name=input('Enter the filename : ')
    file=open(file_name)
    content=file.read()
    l=content.split('\n')
    number_of_lists=l[0]
    lists=[i.split() for i in l[1:]]
    return number_of_lists,lists


def list_encloser(l):
    u = ''
    m = ''
    le=0
    str_list=list(map(str,l))
    for i in str_list:
        if le<len(i):
            le=len(i)

    for i in range(len(l)):
        u += '+{}'.format('-'*le)
        m += ('|{}'.format(str_list[i])+' '*(le-len(str_list[i])))
    u += '+'
    m += '|'
    print(u)
    print(m)
    print(u)


#list_encloser([1,2,3,4,5,6,7,8,9])

def left_rotator(l):
    ans1=l[1:]
    ans1.append(l[0])
    return ans1
def right_rotator(l):
    ans2=[l[-1]]
    for i in l[:-1]:
        ans2.append(i)
    return ans2

#print(right_rotator([5, 1, 2, 3, 4]))
#def list_rotator(type_of_rotation,number_of_rotations,lst):

def rotator(type_of_rotation,number_of_rotations,lst):
    if type_of_rotation=='L':
        for i in range(int(number_of_rotations)):
            lst=left_rotator(lst)
        list_encloser(lst)
    if type_of_rotation=='R':
        for i in range(int(number_of_rotations)):
            lst=right_rotator(lst)
        list_encloser(lst)

#rotator('R',1,[1,2,3,4,2,3,1,6])
a,b=main()
#print(a,b)
#list_encloser([2,4,6,8,1000])
for i in b:
    rotator(i[0],i[1],i[2:])






