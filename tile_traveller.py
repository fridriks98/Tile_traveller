xy_pos = 1

E = "(E)ast"
N = "(N)orth"
S = "(S)outh"
W = "(W)est"

while True:
    Bool = True
    if xy_pos == 7:
        print("Victory!")
        break
    elif xy_pos == 8:
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
    
    while Bool:
        direction = input("Direction: ").lower()
        if direction == 'e' and xy_pos in(2,3,6):
            xy_pos += 3
            Bool = False
        elif direction == 'n' and xy_pos in(1,2,4,8):
            xy_pos += 1
            Bool = False
        elif direction == 's' and xy_pos in (2,3,5,8,9):
            xy_pos -= 1
            Bool = False
        elif direction == 'w' and xy_pos in (5,6,9):
            xy_pos -= 3
            Bool = False

        if Bool:
            print("Not a valid direction!")
             
        
