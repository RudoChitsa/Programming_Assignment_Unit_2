#define a function to print one blank line
def new_line():
    print('.__________________________________________________')

#a function print 3 blank lines
def three_lines():
    new_line()
    new_line()
    new_line()

#a function called nine_lines that uses the function three_lines.
#Using it to print 9 blank lines
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

#a funciton to print 25 blank lines using the above functions
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    new_line()
    three_lines()

# to print 9 lines
print("Printing 9 lines")
nine_lines()

# to print 25 lines
print("Calling clearScreen()")
clear_screen()


