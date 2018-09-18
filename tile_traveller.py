x_pos = 1
y_pos = 1

word_list = ['e', 'E', 'n', 'N', 's', 'S', 'w', 'W']
Direction_list = ["(E)ast", "(N)orth",'(S)outh', "(W)est"]

direction = input("Direction: ")

if direction in word_list:
    if y_pos == 1:
        print("You can travel: {}".format(Direction_list[1]))


