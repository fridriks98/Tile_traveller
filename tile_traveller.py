x_pos = 1
y_pos = 1

E = "(E)ast"
N = "(N)orth"
S = "(S)outh"
W = "(W)est"

while True:
    Bool = True
    if x_pos == 3 and y_pos == 1:
        print("Victory!")
        break
    elif x_pos == 3 and y_pos == 2:
        print("You can travel: {} or {}.".format(N,S))
    elif x_pos == 3 and y_pos == 3:
        print("You can travel: {} or {}.".format(S,W))
    elif x_pos == 2 and y_pos == 1:
        print("You can travel: {}.".format(N))
    elif x_pos == 2 and y_pos == 2:
        print("You can travel: {} or {}.".format(S,W))
    elif x_pos == 2 and y_pos == 3:
        print("You can travel: {} or {}.".format(E,W))
    elif x_pos == 1 and y_pos == 1:          
        print("You can travel: {}.".format(N))
    elif x_pos == 1 and y_pos == 2:
        print("You can travel: {} or {} or {}.".format(E,N,S))
    elif x_pos == 1 and y_pos == 3:
        print("You can travel: {} or {}.".format(E,S))
    
    while Bool == True:
        direction = input("Direction: ").lower()
        if direction == 'e' and x_pos != 3:
            x_pos += 1
            Bool = False
        elif direction == 'n' and y_pos != 3:
            y_pos += 1
            Bool = False
        elif direction == 's' and y_pos != 1:
            y_pos -= 1
            Bool = False
        elif direction == 'w' and x_pos != 1:
            x_pos -= 1
            Bool = False
        if Bool == True:
            print("Not a valid direction!")
             
        
