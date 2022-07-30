def h1_formatter(s):
    print("//"+"="*(len(s)+2)+"\\"+"\\")
    print("|| "+s.upper()+" ||")
    print("\\"+"\\"+"="*(len(s)+2)+"//")
def h2_formatter(s):
    print(" "+s+" ")
    print("-"*(len(s)+2))
def ol_formatter(s,k):
    print(str(k)+"."+" "+s)
def ul_formatter(s):
    print(">"+" "+s)

l=["h1 the","h2 winter","ol is","ol coming","ol hello","ul be","ol ready","ol go","pp friend"]
ol_=False
x=1
for i in l:
    if ol_:
        x+=1
        if i[:2]=="ol":
            ol_formatter(i[3:],x)
            continue
        else:
            ol_=False
            x=1
            if i[:2] == "h1":
                h1_formatter(i[3:])
            if i[:2] == "h2":
                h2_formatter(i[3:])
            if i[:2] == "ul":
                ul_formatter(i[3:])
            if i[:2] == "pp":
                print(i[3:])
            continue

    if i[:2]=="h1":
        h1_formatter(i[3:])
    if i[:2]=="h2":
        h2_formatter(i[3:])
    if i[:2]=="ol":
        ol_formatter(i[3:],x)
        ol_=True
    if i[:2] == "ul":
        ul_formatter(i[3:])
    if i[:2] == "pp":
        print(i[3:])
