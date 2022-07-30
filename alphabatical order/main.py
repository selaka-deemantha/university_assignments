def oreder_checker(s):
    in_order=True
    rev_order=True
    ss=[i for i in s if i.isalpha()]
    for i in range(len(ss)-1):
        if ord(ss[i].lower())==ord(ss[i+1].lower()):
            continue
        elif ord(ss[i].lower())>ord(ss[i+1].lower()):
            in_order=False
        elif ord(ss[i].lower())<ord(ss[i+1].lower()):
            rev_order=False
    if in_order:
        print(s+" IN ORDER")
    elif rev_order:
        print(s+" IN REVERSE ORDER")
    else:
        print(s+" NOT IN ORDER")
oreder_checker("Wro123ngeD")

