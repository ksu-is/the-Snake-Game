import tkinter 

import random

GAME_WIDTH = 750
GAME_HEIGHT = 750
SPEED = 50
SPACE_SIZE = 50
BODYPARTS = 3
SNAKECOLOR = '#00FFFF'
FOODCOLOR = 'FF0000'
BACKGROUND_COLOR = '#FFFFFF'

class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_dic(new_direction):
    pass

def check_collisions():
    pass

def gameover():
    pass

window = Tk()
window.title('Snake Game')
window.resizable (False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score),font=('arial',40))
label.pack()

canvas = Canvas(window, bg = BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()

window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
        
y = (screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()
