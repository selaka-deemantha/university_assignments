def anagram_checker(str1,str2):
    str1=[i.lower() for i in str1 if i.isalpha()]
    str2=[i.lower() for i in str2 if i.isalpha()]
    if len(str1)!=len(str2):
        return "These are not anagrams"
    for i in str1:
        if i not in str2:
            return "These are not anagrams"
    return "These are anagrams"
def valid_inputs_checker(s):
    for i in s:
        if not i.isalpha() and i!=" ":
            return False
    return True


#print(anagram_checker("Eleven p23lus TOW","Twel!ve plus One"))
while True:
    str1=input("ENTER STRING ONE : ")
    str2=input("ENTER STRING TWO : ")
    if valid_inputs_checker(str1) and valid_inputs_checker(str2):
        print(anagram_checker(str1,str2))
        break
    else:
        print("inputs contain non alphabatical characters try again")


