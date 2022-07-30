def door_knob(s):
    for i in range(len(s)-1):
        if s[i]=="D" and (s[i+1]=="D" or s[i+1]=="O"):
            print(1)
            return "RUINED"
        elif s[i]=="R" and s[i+1]!="E":
            print(2)
            return "RUINED"
        elif s[i]=="O" and (s[i+1]=="D" or s[i+1]=="E" or s[i+1]=="T"):
            print(3)
            return "RUINED"
        elif s[i]=="E" and (s[i+1]!="T" and s[i+1]!="D"):
            print(4)
            return "RUINED"
        elif s[i]=="T" and (s[i+1]!="R" and s[i+1]!="O"):
            print(5)
            return "RUINED"
        elif s[i]=="S" and (s[i+1]=="S" or s[i+1]=="E" or s[i+1]=="T" or s[i+1]=="D"):
            print(6)
            return "RUINED"
    return "OPEND"
print(door_knob("SOORETS"))


