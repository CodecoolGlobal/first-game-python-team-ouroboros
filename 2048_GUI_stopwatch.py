from tkinter import *
from tkinter import ttk
from random import randint
from copy import deepcopy
import sys
import os
from tkinter import messagebox


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
    print(table)
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
    if table[0][0] != 0:
        cell_1.set(table[0][0])
    else:
        cell_1.set('  ')
    if table[0][1] != 0:
        cell_2.set(table[0][1])
    else:
        cell_2.set('  ')
    if table[0][2] != 0:
        cell_3.set(table[0][2])
    else:
        cell_3.set('  ')
    if table[0][3] != 0:
        cell_4.set(table[0][3])
    else:
        cell_4.set('  ')
    if table[1][0] != 0:
        cell_5.set(table[1][0])
    else:
        cell_5.set('  ')
    if table[1][1] != 0:
        cell_6.set(table[1][1])
    else:
        cell_6.set('  ')
    if table[1][2] != 0:
        cell_7.set(table[1][2])
    else:
        cell_7.set('  ')
    if table[1][3] != 0:
        cell_8.set(table[1][3])
    else:
        cell_8.set('  ')
    if table[2][0] != 0:
        cell_9.set(table[2][0])
    else:
        cell_9.set('  ')
    if table[2][1] != 0:
        cell_10.set(table[2][1])
    else:
        cell_10.set('  ')
    if table[2][2] != 0:
        cell_11.set(table[2][2])
    else:
        cell_11.set('  ')
    if table[2][3] != 0:
        cell_12.set(table[2][3])
    else:
        cell_12.set('  ')
    if table[3][0] != 0:
        cell_13.set(table[3][0])
    else:
        cell_13.set('  ')
    if table[3][1] != 0:
        cell_14.set(table[3][1])
    else:
        cell_14.set('  ')
    if table[3][2] != 0:
        cell_15.set(table[3][2])
    else:
        cell_15.set('  ')
    if table[3][3] != 0:
        cell_16.set(table[3][3])
    else:
        cell_16.set('  ')
    cell_17.set(digital_timer)

def callback(event):

    global table, status

    if status == 'New round':

        prev_table = deepcopy(table)

        if event.keysym == 'Up':
            table = slide_up(table)
        elif event.keysym == 'Down':
            table = slide_down(table)
        elif event.keysym == 'Right':
            table = slide_right(table)
        elif event.keysym == 'Left':
            table = slide_left(table)
        
        if prev_table != table:
            insert_number(table)
        update_GUI_cells()   
        if status_check(table) != "New round":
            status = status_check(table)
            if status == 'You win':
                #messagebox.askretrycancel("2048 message","You win!")
                popupmsg('You win!')
            else:
                #messagebox.askretrycancel("2048 message","You lose!")
                popupmsg('You lose!')
        #print(status)
    
    
    update_GUI_cells()

def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Restart", command = restart_game)
    B1.pack()
    B2 = ttk.Button(popup, text="Quit", command = combine_funcs(root.destroy, popup.destroy))
    B2.pack()
    popup.mainloop()

"""def quit_game():
    root.destroy()"""

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func 


def restart_game():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def timer(time):
    def count(): 
        if running: 
            global counter
            global digital_timer 
            display=str(time) 
            time.config(text=display)   
  
            # label.after(arg1, arg2) delays by  
            # first argument given in milliseconds 
            # and then calls the function given as second argument. 
            # Generally like here we need to call the  
            # function in which it is present repeatedly. 
            # Delays by 1000ms=1 seconds and call count again. 
            time.after(1000, count)  
            counter += 1
            if counter < 10: 
                digital_timer = f'00:0{counter % 15}'
            else:
                if (counter // 15 < 10) and (counter % 15 < 10): 
                    digital_timer = f'0{counter // 15}:0{counter % 15}'
                elif (counter // 15 < 10) and (counter % 15 >= 10):               
                    digital_timer = f'0{counter // 15}:{counter % 15}'
                else:
                    if counter % 15 < 10:
                        digital_timer = f'{counter // 15}:0{counter % 15}'
                    else:
                        digital_timer = f'{counter // 15}:{counter % 15}'


            #To update the timer continously
            update_GUI_cells()
    # Triggering the start of the counter. 
    count()
 

def start_timer(time): 
    global running 
    running=True
    timer(time) 


table = starting_table()
status = "New round"

counter = -1
running = False
digital_timer = '00:00'

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
cell_17 = StringVar()

update_GUI_cells()

# frame styles

gui_style = ttk.Style()
gui_style.configure('TButton', foreground='#334353')
gui_style.configure('outer.TFrame', background='#363740')
gui_style.configure('cell.TFrame', background='#351f36')
gui_style.configure('TLabel', background='#351f36', foreground='#ccc497')

#the main frame
mainframe = ttk.Frame(root, width=1500, height=600, padding=10, style='outer.TFrame')
mainframe.grid()

#the game board occupying the left side of the main frame

time = ttk.Frame(mainframe, width=120, height=50, relief='raised', style='TLabel')
time.grid(row=0, column=0)
game_board = ttk.Frame(mainframe, width=1200, height=600, relief='raised')
game_board.grid(row=1, column=0)


#the individual frames of the game board

frame_1 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_1.grid(row=0, column=0, sticky='N,W,S,E')
frame_1.configure(height=100,width=100)
frame_1.grid_propagate(0)

frame_2 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_2.grid(row=0, column=1, sticky='N,W,S,E')
frame_2.configure(height=100,width=100)
frame_2.grid_propagate(0)

frame_3 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_3.grid(row=0, column=2, sticky='N,W,S,E')
frame_3.configure(height=100,width=100)
frame_3.grid_propagate(0)

frame_4 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_4.grid(row=0, column=3, sticky='N,W,S,E')
frame_4.configure(height=100,width=100)
frame_4.grid_propagate(0)

frame_5 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_5.grid(row=1, column=0, sticky='N,W,S,E')
frame_5.configure(height=100,width=100)
frame_5.grid_propagate(0)

frame_6 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_6.grid(row=1, column=1, sticky='N,W,S,E')
frame_6.configure(height=100,width=100)
frame_6.grid_propagate(0)

frame_7 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_7.grid(row=1, column=2, sticky='N,W,S,E')
frame_7.configure(height=100,width=100)
frame_7.grid_propagate(0)

frame_8 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_8.grid(row=1, column=3, sticky='N,W,S,E')
frame_8.configure(height=100,width=100)
frame_8.grid_propagate(0)

frame_9 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_9.grid(row=2, column=0, sticky='N,W,S,E')
frame_9.configure(height=100,width=100)
frame_9.grid_propagate(0)

frame_10 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_10.grid(row=2, column=1, sticky='N,W,S,E')
frame_10.configure(height=100,width=100)
frame_10.grid_propagate(0)

frame_11 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_11.grid(row=2, column=2, sticky='N,W,S,E')
frame_11.configure(height=100,width=100)
frame_11.grid_propagate(0)

frame_12 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_12.grid(row=2, column=3, sticky='N,W,S,E')
frame_12.configure(height=100,width=100)
frame_12.grid_propagate(0)

frame_13 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_13.grid(row=3, column=0, sticky='N,W,S,E')
frame_13.configure(height=100,width=100)
frame_13.grid_propagate(0)

frame_14 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_14.grid(row=3, column=1, sticky='N,W,S,E')
frame_14.configure(height=100,width=100)
frame_14.grid_propagate(0)

frame_15 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_15.grid(row=3, column=2, sticky='N,W,S,E')
frame_15.configure(height=100,width=100)
frame_15.grid_propagate(0)

frame_16 = ttk.Frame(game_board, padding=50, relief='raised', style='cell.TFrame')
frame_16.grid(row=3, column=3, sticky='N,W,S,E')
frame_16.configure(height=100,width=100)
frame_16.grid_propagate(0)


#labels for frames on game board
label_frame_1 = ttk.Label(frame_1, textvariable=cell_1, style='TLabel')
label_frame_1.place(anchor="center")
label_frame_1.config(font=("Arial", 35))
label_frame_2 = ttk.Label(frame_2, textvariable=cell_2, style='TLabel')
label_frame_2.place(anchor="center")
label_frame_2.config(font=("Arial", 35))
label_frame_3 = ttk.Label(frame_3, textvariable=cell_3, style='TLabel')
label_frame_3.place(anchor="center")
label_frame_3.config(font=("Arial", 35))
label_frame_4 = ttk.Label(frame_4, textvariable=cell_4, style='TLabel')
label_frame_4.place(anchor="center")
label_frame_4.config(font=("Arial", 35))
label_frame_5 = ttk.Label(frame_5, textvariable=cell_5, style='TLabel')
label_frame_5.place(anchor="center")
label_frame_5.config(font=("Arial", 35))
label_frame_6 = ttk.Label(frame_6, textvariable=cell_6, style='TLabel')
label_frame_6.place(anchor="center")
label_frame_6.config(font=("Arial", 35))
label_frame_7 = ttk.Label(frame_7, textvariable=cell_7, style='TLabel')
label_frame_7.place(anchor="center")
label_frame_7.config(font=("Arial", 35))
label_frame_8 = ttk.Label(frame_8, textvariable=cell_8, style='TLabel')
label_frame_8.place(anchor="center")
label_frame_8.config(font=("Arial", 35))
label_frame_9 = ttk.Label(frame_9, textvariable=cell_9, style='TLabel')
label_frame_9.place(anchor="center")
label_frame_9.config(font=("Arial", 35))
label_frame_10 = ttk.Label(frame_10, textvariable=cell_10, style='TLabel')
label_frame_10.place(anchor="center")
label_frame_10.config(font=("Arial", 35))
label_frame_11 = ttk.Label(frame_11, textvariable=cell_11, style='TLabel')
label_frame_11.place(anchor="center")
label_frame_11.config(font=("Arial", 35))
label_frame_12 = ttk.Label(frame_12, textvariable=cell_12, style='TLabel')
label_frame_12.place(anchor="center")
label_frame_12.config(font=("Arial", 35))
label_frame_13 = ttk.Label(frame_13, textvariable=cell_13, style='TLabel')
label_frame_13.place(anchor="center")
label_frame_13.config(font=("Arial", 35))
label_frame_14 = ttk.Label(frame_14, textvariable=cell_14, style='TLabel')
label_frame_14.place(anchor="center")
label_frame_14.config(font=("Arial", 35))
label_frame_15 = ttk.Label(frame_15, textvariable=cell_15, style='TLabel')
label_frame_15.place(anchor="center")
label_frame_15.config(font=("Arial", 35))
label_frame_16 = ttk.Label(frame_16, textvariable=cell_16, style='TLabel')
label_frame_16.place(anchor="center")
label_frame_16.config(font=("Arial", 35))


#label for timer frame
label_frame_17 = ttk.Label(time, textvariable=cell_17, style='TLabel')
label_frame_17.place(x=60, y=25, anchor="center")
label_frame_17.config(font=("Arial", 30))

#stopwatch - needs to be after the label_frame_17 variable was created
start_timer(label_frame_17)



#event handling for control control board
root.bind('<Key>', callback)


root.mainloop()
