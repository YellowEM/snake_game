# import pygame
from tkinter import *

game_width = 500
game_height = 500
snake_item = 10
snake_color1='red'
snake_color2='yellow'

tk = Tk()
tk.title('Игра Змейка на Python')
tk.resizable (0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=game_width, height=game_height, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

def snake_paint_item(canvas, x, y):
    canvas.create_rectangle(x*snake_item, y*snake_item,
                            x*snake_item+snake_item, y*snake_item+snake_item,fill=snake_color1)
    canvas.create_rectangle(x*snake_item+2, y*snake_item+2,
                            x*snake_item+snake_item-2, y*snake_item+snake_item-2,fill=snake_color2)
snake_paint_item(canvas, 1, 1)
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
