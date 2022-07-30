def is_win(l):
    if len(l) < 3:
        return False
    else:
        if (1 in l and 2 in l and 3 in l) or (4 in l and 5 in l and 6 in l) or (7 in l and 8 in l and 9 in l):
            return True
        elif (1 in l and 4 in l and 7 in l) or (2 in l and 5 in l and 8 in l) or (3 in l and 6 in l and 9 in l):
            return True
        elif (1 in l and 5 in l and 9 in l) or (3 in l and 5 in l and 7 in l):
            return True
        else:
            return False
pl_1=[]
pl_2=[]
tot=[1,2,3,4,5,6,7,8,9]
i=2
not_win=True
while not_win:
    if i%2==0:
        a=int(input("Player 1 : "))
        if a not in pl_2 and a not in pl_1:
            if a in tot:
                pl_1.append(a)
                i+=1
                if is_win(pl_1):
                    print("player 1 wins")
                    break

            else:
                print("out of the range")
                continue
        else:
            print("this space is filled")
            continue
    if i%2==1:
        a=int(input("player 2 : "))
        if a not in pl_2 and a not in pl_1:
            if a in tot:
                pl_2.append(a)
                i += 1
                if is_win(pl_2):
                    print("player 2 wins")
                    break

            else:
                print("out of the range\ntry again")
                continue
        else:
            print("this space is filled\ntry again")
            continue


