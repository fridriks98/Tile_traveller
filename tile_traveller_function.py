def xy_position(xy_pos):
    E = "(E)ast"
    N = "(N)orth"
    S = "(S)outh"
    W = "(W)est"
    if xy_pos == 8:
        print("You can travel: {} or {}.".format(N,S))
    elif xy_pos == 5 or xy_pos == 9:
        print("You can travel: {} or {}.".format(S,W))
    elif xy_pos == 6:
        print("You can travel: {} or {}.".format(E,W))
    elif (xy_pos == 1 or xy_pos == 4):          
        print("You can travel: {}.".format(N))
    elif xy_pos == 2:
        print("You can travel: {} or {} or {}.".format(N,E,S))
    elif xy_pos == 3:
        print("You can travel: {} or {}.".format(E,S))
    
    return xy_pos

def which_direction(direction, xy_pos):
    if direction == 'e' and xy_pos in(2,3,6):
        xy_pos += 3
    elif direction == 'n' and xy_pos in(1,2,4,8):
        xy_pos += 1
    elif direction == 's' and xy_pos in (2,3,5,8,9):
        xy_pos -= 1
    elif direction == 'w' and xy_pos in (5,6,9):
        xy_pos -= 3
            
    return xy_pos

def boolean(xy_pos):
    print("Not a valid direction!")
    return True
    
xy_pos = 1    

while xy_pos != 7:
    Bool = True
    xy_pos = xy_position(xy_pos)
    
    while Bool == True:
        direction = input("Direction: ").lower()
        xy_new = which_direction(direction,xy_pos)
        if xy_new == xy_pos:
            Bool = boolean(xy_pos)
        else:
            Bool = False
        xy_pos = xy_new

print("Victory!") 