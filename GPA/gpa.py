



let_dict={"A":4.0,"B":2.0,"C":3.0,"D":0.0}

#print(let_dict["A"])

def main():
    file=open("g.txt")
    content=file.read().split("\n")
    num_sub,num_let=content[0].split()
    a=content[1].split()
    b=content[2].split()
    marks=[]
    for i in range(int(num_sub)):
        marks.append([a[i],int(b[i])])
    let_dict={}
    for i in range(int(num_let)):
        l,v=content[i+3].split()
        let_dict[l]=float(v)
    return let_dict,marks


def gpa_cal(letter_dic,marks):
    s=0
    k=0
    for i in marks:
        s+=i[1]*letter_dic[i[0]]
        k+=i[1]
    ans=round(s/k,2)
    state=True
    grade=0
    g=""
    for i in letter_dic.keys():
        if state:
            grade=abs(ans-letter_dic[i])
            state=False
        if grade>=abs(ans-letter_dic[i]):
            grade=abs(ans-letter_dic[i])
            g=i
            #print(g)


    return ans,g

letter_dict=main()[0]
marks=main()[1]

print(gpa_cal(letter_dict,marks))







