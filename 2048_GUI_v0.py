from tkinter import *
from tkinter import ttk

cells = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]

def change_cell(event):
    pass
    global cells
    print((event))
    print(type(event.x))
    if cells[0][0] == 1:
        cells[0][0] = 0
    else:
        cells[0][0] = 1
    cell_1.set(cells[0][0])

def root_destroy():
    root.destroy()

def callback(event):
    if event.keysym == 'Up':
        print('Going up!')
    elif event.keysym == 'Down':
        print('Going down!')
    elif event.keysym == 'Left':
        print('Turning left!')
    elif event.keysym == 'Right':
        print('Turning right!')
    elif event.keysym == 'Escape':
        root.destroy()

def callback_arrow_up(event):
    print('up')
def callback_arrow_down(event):
    print('down')
def callback_arrow_left(event):
    print('left')
def callback_arrow_right(event):
    print('right')

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

cell_1.set(cells[0][0])
cell_2.set(cells[0][1])
cell_3.set(cells[0][2])
cell_4.set(cells[0][3])
cell_5.set(cells[1][0])
cell_6.set(cells[1][1])
cell_7.set(cells[1][2])
cell_8.set(cells[1][3])
cell_9.set(cells[2][0])
cell_10.set(cells[2][1])
cell_11.set(cells[2][2])
cell_12.set(cells[2][3])
cell_13.set(cells[3][0])
cell_14.set(cells[3][1])
cell_15.set(cells[3][2])
cell_16.set(cells[3][3])


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
ttk.Button(controls_row5, text='Restart').grid(row=0, column=0, sticky='N,W,S,E')
ttk.Button(controls_row6, text='Quit', command=root_destroy).grid(row=0, column=0, sticky='N,W,S,E')

#event handling for game board
frame_1.bind('<Button-1>', change_cell)
frame_2.bind('<Button-1>', change_cell)
frame_3.bind('<Button-1>', change_cell)
frame_4.bind('<Button-1>', change_cell)
frame_5.bind('<Button-1>', change_cell)
frame_6.bind('<Button-1>', change_cell)
frame_7.bind('<Button-1>', change_cell)
frame_8.bind('<Button-1>', change_cell)
frame_9.bind('<Button-1>', change_cell)
frame_10.bind('<Button-1>', change_cell)
frame_11.bind('<Button-1>', change_cell)
frame_12.bind('<Button-1>', change_cell)
frame_13.bind('<Button-1>', change_cell)
frame_14.bind('<Button-1>', change_cell)
frame_15.bind('<Button-1>', change_cell)
frame_16.bind('<Button-1>', change_cell)

#event handling for control control board
root.bind('<Key>', callback)
up_arrow.bind('<Button-1>', callback_arrow_up)
left_arrow.bind('<Button-1>', callback_arrow_left)
right_arrow.bind('<Button-1>', callback_arrow_right)
down_arrow.bind('<Button-1>', callback_arrow_down)
controls_row1_col1.bind('<Button-1>', callback_arrow_up)
controls_row2_col0.bind('<Button-1>', callback_arrow_left)
controls_row2_col2.bind('<Button-1>', callback_arrow_right)
controls_row3_col1.bind('<Button-1>', callback_arrow_down)

root.mainloop()
