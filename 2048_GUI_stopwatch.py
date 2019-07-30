from tkinter import *
from tkinter import ttk
from random import randint
from copy import deepcopy
import sys
import os


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

def new_game(start):
    if input("New game? (y/n)") is "y":
        start = "New game"
    else:
        start = "End game"
    return start


# GUI functions:

def update_GUI_cells():
    cell_1.set(table[0][0])
    cell_2.set(table[0][1])
    cell_3.set(table[0][2])
    cell_4.set(table[0][3])
    cell_5.set(table[1][0])
    cell_6.set(table[1][1])
    cell_7.set(table[1][2])
    cell_8.set(table[1][3])
    cell_9.set(table[2][0])
    cell_10.set(table[2][1])
    cell_11.set(table[2][2])
    cell_12.set(table[2][3])
    cell_13.set(table[3][0])
    cell_14.set(table[3][1])
    cell_15.set(table[3][2])
    cell_16.set(table[3][3])

def callback(event):
    global table
    if event.keysym == 'Up':
        slide_up(table)
        print(table)
    elif event.keysym == 'Down':
        slide_down(table)
    elif event.keysym == 'Right':
        slide_right(table)
    elif event.keysym == 'Left':
        slide_left(table)
    
    #insert_number(table)
    update_GUI_cells()

def quit_game():
    root.destroy()


def restart_game():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    

#second counter of the stopwatch    
def counter_label(label):

    
    def count(): 
        if running: 
            global counter 
  
            display=str(counter) 
  
            label['text']=display   # Or label.config(text=display) 
  
            # label.after(arg1, arg2) delays by  
            # first argument given in milliseconds 
            # and then calls the function given as second argument. 
            # Generally like here we need to call the  
            # function in which it is present repeatedly. 
            # Delays by 1000ms=1 seconds and call count again. 
            label.after(1000, count)  
            counter += 1
  
    # Triggering the start of the counter. 
    count()   

# start function of the stopwatch 
def start_timer(label): 
    global running 
    running=True
    counter_label(label) 
    # start['state']='disabled'
    # stop['state']='normal'
    # reset['state']='normal'


root = Tk()
root.title('2048')

cell_1 = StringVar()
cell_2 = StringVar()
cell_3 = StringVar()
cell_4 = StringVar()
cell_5 = StringVar()
cell_6 = StringVar()
cell_7 = StringVar()
cell_8 = StringVar()
cell_9 = StringVar()
cell_10 = StringVar()
cell_11 = StringVar()
cell_12 = StringVar()
cell_13 = StringVar()
cell_14 = StringVar()
cell_15 = StringVar()
cell_16 = StringVar()

#the main frame
mainframe = ttk.Frame(root, width=1500, height=600, padding=10)
mainframe.grid()

#the game board occupying the left side of the main frame
game_board = ttk.Frame(mainframe, width=1000, height=600, relief='raised')
game_board.grid(row=0, column=0)

#the controls occupying the right side of the main frame
controls = ttk.Frame(mainframe, width=500, height=600)
controls.grid(row=0, column=1)

#the sub-frames of the control board
controls_row1 = ttk.Frame(controls, width=500, height=125)
controls_row1.grid(row=0, column=0)

controls_row2 = ttk.Frame(controls, width=500, height=125)
controls_row2.grid(row=1, column=0)

controls_row3 = ttk.Frame(controls, width=500, height=125)
controls_row3.grid(row=2, column=0)

controls_row4 = ttk.Frame(controls, width=500, height=125)
controls_row4.grid(row=3, column=0)

controls_row5 = ttk.Frame(controls, width=500, height=125, padding=15)
controls_row5.grid(row=4, column=0)

controls_row6 = ttk.Frame(controls, width=500, height=125, padding=15)
controls_row6.grid(row=5, column=0)

controls_row1_col0 = ttk.Frame(controls_row1, width=50, height=50)
controls_row1_col0.grid(row=0, column=0)

controls_row1_col1 = ttk.Frame(controls_row1, width=50, height=50, padding=10, relief='raised')
controls_row1_col1.grid(row=0, column=1)

controls_row1_col2 = ttk.Frame(controls_row1, width=50, height=50)
controls_row1_col2.grid(row=0, column=2)

controls_row2_col0 = ttk.Frame(controls_row2, width=50, height=50, padding=10, relief='raised')
controls_row2_col0.grid(row=1, column=0)

controls_row2_col1 = ttk.Frame(controls_row2, width=50, height=50)
controls_row2_col1.grid(row=1, column=1)

controls_row2_col2 = ttk.Frame(controls_row2, width=50, height=50, padding=10, relief='raised')
controls_row2_col2.grid(row=1, column=2)

controls_row3_col0 = ttk.Frame(controls_row3, width=50, height=50)
controls_row3_col0.grid(row=2, column=0)

controls_row3_col1 = ttk.Frame(controls_row3, width=50, height=50, padding=10, relief='raised')
controls_row3_col1.grid(row=2, column=1)

controls_row3_col2 = ttk.Frame(controls_row3, width=50, height=50)
controls_row3_col2.grid(row=2, column=2)

controls_row4_col0 = ttk.Frame(controls_row4, width=50, height=50)
controls_row4_col0.grid(row=3, column=0)

controls_row4_col1 = ttk.Frame(controls_row4, width=50, height=50)
controls_row4_col1.grid(row=3, column=1)

controls_row4_col2 = ttk.Frame(controls_row4, width=50, height=50)
controls_row4_col2.grid(row=3, column=2)

#the individual frames of the game board
frame_1 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_1.grid(row=0, column=0, sticky='N,W,S,E')

frame_2 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_2.grid(row=0, column=1, sticky='N,W,S,E')

frame_3 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_3.grid(row=0, column=2, sticky='N,W,S,E')

frame_4 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_4.grid(row=0, column=3, sticky='N,W,S,E')

frame_5 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_5.grid(row=1, column=0, sticky='N,W,S,E')

frame_6 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_6.grid(row=1, column=1, sticky='N,W,S,E')

frame_7 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_7.grid(row=1, column=2, sticky='N,W,S,E')

frame_8 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_8.grid(row=1, column=3, sticky='N,W,S,E')

frame_9 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_9.grid(row=2, column=0, sticky='N,W,S,E')

frame_10 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_10.grid(row=2, column=1, sticky='N,W,S,E')

frame_11 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_11.grid(row=2, column=2, sticky='N,W,S,E')

frame_12 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_12.grid(row=2, column=3, sticky='N,W,S,E')

frame_13 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_13.grid(row=3, column=0, sticky='N,W,S,E')

frame_14 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_14.grid(row=3, column=1, sticky='N,W,S,E')

frame_15 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_15.grid(row=3, column=2, sticky='N,W,S,E')

frame_16 = ttk.Frame(game_board, width=200, height=200, padding=50, relief='raised')
frame_16.grid(row=3, column=3, sticky='N,W,S,E')

#labels for frames on game board
ttk.Label(frame_1, textvariable=cell_1).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_2, textvariable=cell_2).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_3, textvariable=cell_3).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_4, textvariable=cell_4).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_5, textvariable=cell_5).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_6, textvariable=cell_6).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_7, textvariable=cell_7).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_8, textvariable=cell_8).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_9, textvariable=cell_9).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_10, textvariable=cell_10).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_11, textvariable=cell_11).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_12, textvariable=cell_12).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_13, textvariable=cell_13).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_14, textvariable=cell_14).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_15, textvariable=cell_15).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Label(frame_16, textvariable=cell_16).grid(row=0, column=0, sticky='N,W,S,E')

#labels for frames on control game board
up_arrow = ttk.Label(controls_row1_col1, text='\u2b06')
up_arrow.grid(row=0, column=0, sticky='N,W,S,E')
left_arrow = ttk.Label(controls_row2_col0, text='\u2b05')
left_arrow.grid(row=0, column=0, sticky='N,W,S,E')
right_arrow = ttk.Label(controls_row2_col2, text='\u27a1')
right_arrow.grid(row=0, column=2, sticky='N,W,S,E')
down_arrow = ttk.Label(controls_row3_col1, text='\u2b07')
down_arrow.grid(row=0, column=0, sticky='N,W,S,E')
ttk.Button(controls_row5, text='Restart', command=restart_game).grid(row=0, column=0, sticky='N,W,S,E')
ttk.Button(controls_row6, text='Quit', command=quit_game).grid(row=0, column=0, sticky='N,W,S,E')

#StopWatch
start_timer_button = ttk.Button(controls_row4_col0, text='Start timer', width=15, command=lambda:start_timer(label)) 
label = ttk.Label(controls_row4_col2, text='Welcome', foreground='black', font='Verdana 12 bold') 
label.pack()

counter = 0
running = False

table = starting_table()
start_timer_button.pack()




update_GUI_cells()


#event handling for control control board
root.bind('<Key>', callback)


root.mainloop()
