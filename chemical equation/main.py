def fun(lst):
    l=[]
    mul=int(lst[0])
    str=lst[-1]
    for i in range(len(str)):
        if str[i].isnumeric():
            continue
        else:
            if i!=len(str)-1:
                a=str[i]
                if str[i+1].isnumeric():
                    b=int(str[i+1])
                else:
                    b=1
            else:
                a=str[i]
                b=1
            l.append([a,mul*b])
    return l



def atom_sorter(str):
    l=[]
    for i in str.split("+"):
        l1=[]
        if "*" in i:
            l1=i.split("*")
        else:
            l1=["1",i]
        l.append(l1)
    dict={}
    for i in l:
        nl=fun(i)
        for j in nl:
            if j[0] not in dict:
                dict[j[0]]=j[1]
            else:
                dict[j[0]]+=j[1]
    return dict


def matcher(dict1,dict2):
    if len(dict1)!=len(dict2):
        return "INCORRECT"
    for i in dict1:
        if i not in dict2:
            return "INCORRECT"
        if dict1[i]!=dict2[i]:
            return "INCORRECT"
    return "CORRECT"

def main(str1,str2):
    return matcher(atom_sorter(str1),atom_sorter(str2))

print(main("2*H+2*O","1*H2O2"))