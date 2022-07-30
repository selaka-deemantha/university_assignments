while True:
    str1=input("ENTER STRING ONE : ")
    str2=input("ENTER STRING TWO : ")
    new_str1=str1.replace(" ","")
    new_str2=str2.replace(" ","")
    if new_str2.isalpha() and new_str1.isalpha():
        new_str1=sorted(list(new_str1))
        new_str2=sorted(list(new_str2))
        print(new_str1)
        print(new_str2)
        if new_str2==new_str1:
            print("these are anagrams")
        else:
            print("these are not anagrams")
        break
    else:
        print("inputs contain non alphabatical characters please try again")


