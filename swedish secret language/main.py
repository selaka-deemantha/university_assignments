def main(s):
    vow=['a','e','i','o','u']
    ans=""
    for i in s:
        if i.lower() not in vow and i.isalpha():
            ans+=(i+"o"+i.lower())
        else:
            ans+=i
    print(ans)

main("where is god")
