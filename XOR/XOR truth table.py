def XOR_gate(s):
    if len(s)==2:
        if (s[0]=='0' and s[1]=='0') or (s[0]=='1' and s[1]=='1'):
            return '0'
        else:
            return '1'
    else:
        if (s[0]=='0' and s[1]=='0') or (s[0]=='1' and s[1]=='1'):
            return XOR_gate('0' + s[2:])

        else:
            return XOR_gate('1' + s[2:])

#print(XOR_gate('1111111'))
def binary_generator(num):
    if num==0:
        return 0
    if num==1:
        return 1
    else:
        return 10*binary_generator(num//2)+(num%2)
#print(binary_generator(17))

def binary_list(number_of_inputs):
    ans=[]
    for i in range(2**number_of_inputs):
        i=binary_generator(i)
        i='0'*(number_of_inputs-len(str(i))) + str(i)
        ans.append(str(i))
    return ans
#print(binary_list(4))

def tabel_generator(input_list):
    ub=''
    mr=''
    for i in input_list:
        ub+='+'+'-'*len(i)
        mr+='|{}'.format(i)
    ub+='+-+'
    mr+='|Y|'
    lst=binary_list(len(input_list))
    middle=[]
    for j in lst:
        cr=''
        t=0
        for k in j:
            cr+='|{}'.format(k)+' '*(len(input_list[t])-1)
            t+=1
        cr+='|{}|'.format(XOR_gate(j))
        middle.append(cr)


    print(ub)
    print(mr)
    print(ub)
    for i in middle:
        print(i)
    print(ub)
tabel_generator(['q','d'])