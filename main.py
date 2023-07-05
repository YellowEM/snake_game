# import pygame
from tkinter import *
import time
import random

game_width = 500
game_height = 500
snake_item = 10
snake_color1 = 'red'
snake_color2 = 'yellow'
snake_x = 24
snake_y = 24
snake_x_nav = 0
snake_y_nav = 0

snake_list = []
snake_size = 5

virtual_game_x = game_width / snake_item
virtual_game_y = game_height / snake_item


tk = Tk()
tk.title("Игра Змейка на Python")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=game_width, height=game_height, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

present_color1 = 'blue'
present_color2 = 'black'

present_color1 = "blue"
present_color2 = "black"
presents_list = []
presents_size = 5
for i in range(presents_size):
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id1 = canvas.create_oval(x*snake_item,y*snake_item, x*snake_item+snake_item,y*snake_item+snake_item,fill=present_color2)
    id2 = canvas.create_oval(x*snake_item+2,y*snake_item+2,x*snake_item+snake_item-2,y*snake_item+snake_item-2,fill=present_color1)
    presents_list.append([x, y, id1, id2])
    presents_list.appen, ([x, y, id1, id2])

def snake_paint_item(canvas, x, y):
    global snake_list
    id1 = canvas.create_rectangle(x * snake_item, y * snake_item, x * snake_item + snake_item,
                                  y * snake_item + snake_item, fill=snake_color2)
    id2 = canvas.create_rectangle(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
                                  y * snake_item + snake_item - 2, fill=snake_color1)
    snake_list.append([x, y, id1, id2])
    print(snake_list)


snake_paint_item(canvas, snake_x, snake_y)


def check_can_we_delete_snake_item():
    if len(snake_list) >= snake_size:
        temp_item = snake_list.pop(0)
        print(temp_item)
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])


def snake_move(event):
    global snake_x
    global snake_y
    if event.keysym == 'Up':
        snake_x_nav = 0
        snake_y_nav = -1
        check_can_we_delete_snake_item()
    if event.keysym == 'Down':
        snake_x_nav = 0
        snake_y_nav = 1
        check_can_we_delete_snake_item()
    if event.keysym == 'Left':
        snake_x_nav = -1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    if event.keysym == 'Right':
        snake_x_nav = 1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)


canvas.bind_all("<KeyPress-Left>", snake_move)
canvas.bind_all("<KeyPress-Right>", snake_move)
canvas.bind_all("<KeyPress-Up>", snake_move)
canvas.bind_all("<KeyPress-Down>", snake_move)
tk.mainloop()

# SIZE_BLOCK = 20
# FRAME_COLOR = (0, 255, 204)
# WHITE = (255, 255, 255)
# BLUE = (100, 255, 255)
# size = [500, 600]
# COUNT_BLOCKS = 20
# MARGIN = 1
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption('Змейка')
# while True:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#     screen.fill(FRAME_COLOR)
#     for row in range(COUNT_BLOCKS):
#         for column in range(COUNT_BLOCKS):
#             if (row + column) % 2 == 0:
#                 color = BLUE
#             else:
#                 color = WHITE
#             pygame.draw.rect(screen, color, [10 + column*SIZE_BLOCK + MARGIN * (column + 1),
#                                              20 + row*SIZE_BLOCK + MARGIN * (row + 1),
#                                              SIZE_BLOCK,
#                                              SIZE_BLOCK])
#
#     pygame.display.flip()
