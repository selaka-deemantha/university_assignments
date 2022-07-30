def dycriptor(s):
    dict={"t":"a","h":"b","e":"c","q":"d","u":"e","i":"f","c":"g","k":"h","b":"i","r":"j","o":"k","w":"l","n":"m","f":"n","x":"o","j":"p","m":"q","p":"r","s":"s","v":"t","l":"u","a":"v","z":"w","y":"x","d":"y","g":"z",}
    ans=""
    for i in s:
        if not i.isalpha():
            ans+=i
        elif i.isupper():
            ans+=dict[i.lower()].upper()
        else:
            ans+=dict[i]
    print(ans)

dycriptor("Cxxq Wleo")