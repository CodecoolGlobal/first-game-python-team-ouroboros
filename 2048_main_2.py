from random import randint
import copy

def starting_table():
    table = [[0] * 4 for row in range(4)]
    starting_coordinates_1 = starting_coordinates_2 = None
    while starting_coordinates_1 == starting_coordinates_2:
        starting_coordinates_1 = [randint(0,3), randint(0,3)]
        starting_coordinates_2 = [randint(0,3), randint(0,3)]
    two_or_four = randint(0,9)
    if two_or_four < 9:
        table[starting_coordinates_1[0]][starting_coordinates_1[1]] = 2 
    else:
        table[starting_coordinates_1[0]][starting_coordinates_1[1]] = 4
    two_or_four = randint(0,9)
    if two_or_four < 9:
        table[starting_coordinates_2[0]][starting_coordinates_2[1]] = 2
    else:
        table[starting_coordinates_2[0]][starting_coordinates_2[1]] = 4   
    return table

def zero_search(table):
    zero_coordinates = []
    for i in range(len(table)):
        for j, zero in enumerate(table[i]):
            if zero == 0:
                    zero_coordinates.append([i, j])
    return zero_coordinates

def status_check(table):
    copy_table= [sorted(row,reverse = True) for row in table]
    if max(max(copy_table)) < 16:
    #if max([max(row) for row in table])<16:
    #if max(max(table)) < 2048:
        if zero_search(table) != []:
            status = "New round"
        elif addable(table):
            status = "New round"
        else:
            status = "End game"
    else:
       status = "You win"
    return status

def addable(table):
    equals = []
    for i in range(len(table)):
        for j in range(4):
            if i != 3 and j != 3:     
                if table[i][j] == table[i][j+1] or table[i][j] == table[i+1][j]:
                    equals.append([i,j])
            if i == 3 and j != 3:
                if table[i][j] == table[i][j+1]:
                    equals.append([i,j])
            if i != 3 and j == 3:
                if table[i][j] == table[i+1][j]:
                    equals.append([i,j])
    return True if equals != [] else False

def remove_all(what, from_where):
    for nested_list in from_where:
        while what in nested_list:
            nested_list.remove(what)

def slide_right(table):
    remove_all(0,table)
    for rows in table:
        if len(rows) == 2:
            if rows[-1] == rows[-2]:
                rows[-1] += rows[-2]
                del rows[-2]
        elif len(rows) == 3:
            if rows[-1] == rows[-2]:
                rows[-1] += rows[-2]
                del rows[-2]
            elif rows[-2] == rows[-3]:
                rows[-2] += rows[-3]
                del rows[-3]  
        elif len(rows) == 4:
                if rows[-1] == rows[-2] and rows[-3] == rows[-4]:
                    rows[-1] += rows[-2]
                    rows[-2] = rows[-3] + rows[-4]
                    del rows[-4]
                    del rows[-3]
                elif rows[-1] == rows[-2]:
                    rows[-1] += rows[-2]
                    del rows[-2]
                elif rows[-2] == rows[-3]:
                    rows[-2] += rows[-3]
                    del rows[-3]  
                elif rows[-3] == rows[-4]:
                    rows[-3] += rows[-4]
                    del rows[-4]
    for i in range(4):
        while len(table[i]) != 4:
            table[i].insert(0,0)    
    return table

def slide_left(table):
    remove_all(0,table)
    for i in range(4):
        if len(table[i]) == 2:
            if table[i][0] == table[i][1]:
                table[i][0] += table[i][1]
                table[i].pop(1)
        elif len(table[i]) == 3:
            if table[i][0] == table[i][1]:
                table[i][0] += table[i][1]
                table[i].pop(1)
            elif table[i][1] == table[i][2]:
                table[i][1] += table[i][2]
                table[i].pop(2)
        elif len(table[i]) == 4:
            if table[i][0] == table[i][1] and table[i][2] == table[i][3]:
                table[i][0] += table[i][1]
                table[i][2] += table[i][3]
                table[i].pop(3)
                table[i].pop(1)
            elif table[i][0] == table[i][1]:
                table[i][0] += table[i][1]
                table[i].pop(1)
            elif table[i][1] == table[i][2]:
                table[i][1] += table[i][2]
                table[i].pop(2)
            elif table[i][2] == table[i][3]:
                table[i][2] += table[i][3]
                table[i].pop(3)
    for i in range(4):
        while len(table[i]) != 4:
            table[i].append(0)
    return table

def rotate(table):
	return [list(row) for row in zip(*table)]

def slide_up(table):
    table = rotate(table)
    slide_left(table)
    table = rotate(table)
    return table

def slide_down(table):
    table = rotate(table)
    slide_right(table)
    table = rotate(table)
    return table

def insert_number(table):
    zero_coordinates = zero_search(table)
    if zero_coordinates != []: 
        number_of_zeroes = len(zero_coordinates)
        random_index = randint(0,number_of_zeroes-1)
        i_j_coordinates = zero_coordinates[random_index]
        i_coordinate = i_j_coordinates[0]
        j_coordinate = i_j_coordinates[1]
        table[i_coordinate][j_coordinate] = 2
    return table

def table_print():
    print("\033c", end="")
    print("""moves: 'w'= up / 's'= down / 'a'=left / 'd'=right
    or enter 'x' to exit """)
    for i in range(4):
        print(table[i])
    print()

def user_input():
    class _Getch:
        """Gets a single character from standard input.  Does not echo to the
    screen."""
        def __init__(self):
            self.impl = _GetchUnix()
        def __call__(self): return self.impl()
    class _GetchUnix:
        def __init__(self):
            import tty, sys
        def __call__(self):
            import sys, tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
    return _GetchUnix()

def new_game(start):
    if input("New game? (y/n)") is "y":
        start = "New game"
    else:
        start = "End game"
    return start

table = []
prev_table = []
start = "New game"
while start == "New game":
    status = "New round"
    table = starting_table()
    table_print()
    while status is "New round":
        prev_table = copy.deepcopy(table)
        x = user_input()
        y = x()
        if y == "w":
            table = slide_up(table)
        elif y == "s":
            table = slide_down(table)
        elif y == "a":
            table = slide_left(table)
        elif y == "d":
            table = slide_right(table)
        elif y == "x":
            if input("Sure to exit?(y/n):") is "y":
                exit()
            else:
                table_print()
        if prev_table != table:
            insert_number(table)
        if status_check(table) != "New round":
            status = status_check(table)
        table_print()
    else:
        if status == "End game":
            print ("No moves left! Game Over!")
            start = new_game(start)
        elif status == "You win": 
            print ("Congrats! You win!")
            start = new_game(start)
else:
    exit()