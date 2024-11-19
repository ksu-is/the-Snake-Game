from tkinter import *

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

    def __init__(self):
        self.body_size = BODYPARTS
        self.coordinates = []
        self.squares = []

        for i in range (0, BODYPARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill= SNAKECOLOR, tag='snake')
            self.squares.append(square)

class Food:
    
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        
        self.coordinates = [x,y]
        
        canvas.create_oval(x,y,x + SPACE_SIZE, fill = FOODCOLOR, tag='FOOD')

def next_turn(snake, food):

        x, y = snake.coordinates [0]

        if direction == 'up':
            y -= SPACE_SIZE
        
        elif direction == 'down':
            y+= SPACE_SIZE
        
        elif direction == 'left':
            x -= SPACE_SIZE

        elif direction == 'right':
            x += SPACE_SIZE

        snake.coordinates.insert(0, (x,y))

        square = canvas.create_rectangle(x, y, x  + SPACE_SIZE, y + SPACE_SIZE)

        snake.squares.insert (0, square)

        del snake.coordinates [-1]

        canvas.delete(snake.squares [-1])

        del snake.squares[-1]

        window.after(SPEED, next_turn, snake, food)


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
        
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()


next_turn(snake, food)
window.mainloop()
