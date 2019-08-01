from random import randint
import copy
from termcolor import colored, cprint


def starting_table():
    table = [[0] * 4 for row in range(4)]
    starting_coordinates_1 = starting_coordinates_2 = None
    while starting_coordinates_1 == starting_coordinates_2:
        starting_coordinates_1 = [randint(0, 3), randint(0, 3)]
        starting_coordinates_2 = [randint(0, 3), randint(0, 3)]
    two_or_four = (randint(0, 9), randint(0, 9))  # 90% nr 2, 10% nr 4 inserted
    if two_or_four[0] < 9:
        table[starting_coordinates_1[0]][starting_coordinates_1[1]] = 2
    else:
        table[starting_coordinates_1[0]][starting_coordinates_1[1]] = 4
    if two_or_four[1] < 9:
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
    copy_table = [sorted(row, reverse=True) for row in table]
    WINNING_CONDITION = 16
    if max(max(copy_table)) < WINNING_CONDITION:
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
                    equals.append([i, j])
            if i == 3 and j != 3:
                if table[i][j] == table[i][j+1]:
                    equals.append([i, j])
            if i != 3 and j == 3:
                if table[i][j] == table[i+1][j]:
                    equals.append([i, j])
    return True if equals != [] else False


def remove_zeros(table):
    for nested_list in table:
        while 0 in nested_list:
            nested_list.remove(0)
    return table


def slide_right(table):
    remove_zeros(table)
    global score
    for rows in table:
        if len(rows) == 2:
            if rows[-1] == rows[-2]:
                rows[-1] += rows[-2]
                del rows[-2]
                score += rows[-1]
        elif len(rows) == 3:
            if rows[-1] == rows[-2]:
                rows[-1] += rows[-2]
                del rows[-2]
                score += rows[-1]
            elif rows[-2] == rows[-3]:
                rows[-2] += rows[-3]
                del rows[-3]
                score += rows[-2]
        elif len(rows) == 4:
            if rows[-1] == rows[-2] and rows[-3] == rows[-4]:
                rows[-1] += rows[-2]
                rows[-2] = rows[-3] + rows[-4]
                del rows[-4]
                del rows[-3]
                score += rows[-1] + rows[-2]
            elif rows[-1] == rows[-2]:
                rows[-1] += rows[-2]
                del rows[-2]
                score += rows[-1]
            elif rows[-2] == rows[-3]:
                rows[-2] += rows[-3]
                del rows[-3]
                score += rows[-2]
            elif rows[-3] == rows[-4]:
                rows[-3] += rows[-4]
                del rows[-4]
                score += rows[-3]
    for i in range(4):
        while len(table[i]) != 4:
            table[i].insert(0, 0)
    return table


def slide_left(table):
    return reverse_rows(slide_right(reverse_rows(table)))


def transpose(table):
    return [list(row) for row in zip(*table)]


def reverse_rows(table):
    return [list(reversed(row)) for row in table]


def slide_up(table):
    return transpose(slide_left(transpose(table)))


def slide_down(table):
    return transpose(slide_right(transpose(table)))


def insert_number(table):
    zero_coordinates = zero_search(table)
    if zero_coordinates != []:
        number_of_zeroes = len(zero_coordinates)
        random_index = randint(0, number_of_zeroes-1)
        i_j_coordinates = zero_coordinates[random_index]
        i_coordinate = i_j_coordinates[0]
        j_coordinate = i_j_coordinates[1]
        table[i_coordinate][j_coordinate] = 2
    return table


def table_print():
    print("\033c", end="")
    table_to_print = copy.deepcopy(table)
    for i in range(4):
        for j in range(4):
            if table_to_print[i][j] == 0:
                table_to_print[i][j] = ""
    print()
    cprint(colored(("THE 2048 GAME".center(33)), "cyan", "on_red", ["bold"]))
    print()
    cprint(colored(f"Score: {score}".ljust(16) + f"High score: {high_score}".rjust(17), "cyan", None, ["bold"]))
    print("-" * 33)
    for i in range(4):
        print("|" + ("".center(7) + "|") * 4)
        print("|" + str(table_to_print[i][0]).center(7) + "|" + str(table_to_print[i][1]).center(7) + "|"
              + str(table_to_print[i][2]).center(7) + "|" + str(table_to_print[i][3]).center(7) + "|")
        print("|" + ("".center(7) + "|") * 4)
        print("-" * 33)
    print()
    cprint(colored("""moves: 'w'= up / 's'= down /
       'a'=left / 'd'=right
       or enter 'x' to exit """, "cyan"))


def user_input():
    class _GetchUnix:
        def __call__(self):
            import sys
            import tty
            import termios
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
    if input("\nNew game? (y/n)") == "y":
        start = "New game"
    else:
        start = "End game"
    return start


def write_high_score(score, high_score):
    if score > high_score:
        with open("high_score.txt", "w", newline="") as f:
            high_score = score
            f.write(str(high_score))


def read_high_score():
    with open("high_score.txt", "r", newline="") as f:
        high_score = int(f.read())
    return(high_score)


start = "New game"
while start == "New game":
    score = 0
    high_score = read_high_score()
    status = "New round"
    table = starting_table()
    table_print()
    while status == "New round":
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
            if input("Sure to exit?(y/n):") == "y":
                exit()
            else:
                table_print()
        if prev_table != table:
            insert_number(table)
        if status_check(table) != "New round":
            status = status_check(table)
        table_print()
    else:
        write_high_score(score, high_score)
        if status == "End game":
            print()
            cprint(colored("No moves left! Game Over!", "red", "on_yellow", ["bold"]))
            start = new_game(start)
        elif status == "You win":
            print()
            cprint(colored(("Congrats! You win!"), "red", "on_green", ["bold"]))
            start = new_game(start)
else:
    exit()
