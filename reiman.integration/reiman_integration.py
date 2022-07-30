
def equ(coe,x):
    ans=0
    for i in range(len(coe)):
        ans+=(coe[i]*((x)**(i)))
    return ans

#print(equ([1,2,3],4))


def main(coeff,intervel,n):
    d_x=(intervel[1]-intervel[0])/n
    k=intervel[0]-(d_x/2)
    area=0
    while(k<=(intervel[1]-(d_x/2))):
        k+=d_x
        #print(k)
        ans=equ(coeff,k)
        area+=(ans*d_x)
    return (area)

print(main([1,2,3],[3,4],100))
print(main([1,0,2,0,5],[10,20],200))
