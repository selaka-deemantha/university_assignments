def bithday_finder(nic):

    year = "19" + nic[:2]
    if int(nic[2:5]) > 500 and int(nic[2:5]) <= 865:
        gender = "F"
        num = int(nic[2:5])-500
    elif int(nic[2:5]) <= 365:
        gender = "M"
        num = int(nic[2:5])
    else:
        return "Invalid nic number"
    month=""
    day=""
    m=[31,29,31,30,31,30,31,31,30,31,30,31]

    finish=True
    j=0
    tot=0
    tot2=0
    while finish:
        tot+=m[j]
        if num<=tot:
            month=str(j+1)
            day=str(num-tot2)
            finish=False
        tot2+=m[j]
        j+=1
    return year+"-"+"0"*(2-len(month))+month+"-"+"0"*(2-len(day))+day+"/"+gender



print(bithday_finder("901912190"))