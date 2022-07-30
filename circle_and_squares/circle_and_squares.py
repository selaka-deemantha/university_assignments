def is_inside_the_circle(radies,c_x,c_y,x,y):
    l=(((c_x-x)**(2))+((c_y-y)**(2)))**(1/2)
    if l<radies:
        return True
    else:
        return False
def rect_grid(w_x,h_y,radies,c_x,c_y):
    tot=0
    for i in range(w_x+1):
        #we add 1/2 units to get the cordinates of the squares
        i+=1/2
        for j in range(h_y+1):
            # we add 1/2 units to get the cordinates of the squares
            j+=1/2
            if is_inside_the_circle(radies,c_x,c_y,i,j):
                tot+=1
    print(tot)
rect_grid(16,13,4,0,3)

