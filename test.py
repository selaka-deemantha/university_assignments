def mostBalancedPartition(parent, files_size):
    # Write your code here
    """
    parent.sort(reverse=True)
    files_size.sort(reverse=True)
    tot=sum(files_size)
    length=len(parent)
    i=0
    lst=[]
    while True:
        a=parent[i]
        idx=length-1-i
        c=files_size[i]
        if idx not in parent:
            lst.append(tot-c)
            par"""
    lst = []
    tot = sum(files_size)
    while True:
        if len(parent) == 1:
            break
        a = parent[-1]
        c = files_size[-1]
        lst.append(abs(tot - c-c))
        if abs(tot - 2*c) == 0:
            return 0
        parent.pop()
        files_size[a] += files_size[-1]
        files_size.pop()
    return (min(lst))

print(mostBalancedPartition([-1,0,1,2],[1,4,3,4]))