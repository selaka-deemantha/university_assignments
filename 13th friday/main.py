#this is very hard question

def leap_year_checker(n):
    if n%4!=0:
        return False
    elif n%100!=0:
        return True
    elif n%400!=0:
        return False
    else:
        return True
def main(y1,y2,d):
    ans=0
    no_l=[31,28,31,30,31,30,31,31,30,31,30,31]
    l=   [31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(y1,y2+1):
        if leap_year_checker(i):
            for j in l:
                if (d+5)%7==5:
                    ans+=1
                d=((j%7)+d)%7
        else:
            for j in no_l:
                if (d+5)%7==5:
                    ans+=1
                d=((j%7)+d)%7
    print(ans)
main(1863,1890,4)




