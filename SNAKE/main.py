import PySimpleGUI as psg
import random
from time import time

TICK = 0.25 # lower TICK = harder difficulty,higher speeds

SIZE = 500
CELLS = 15
CELL_SIZE = SIZE / CELLS
APPLE_EATEN = False
GAME = True
SCORE = 0


SNAKE_BODY = [(10,8),(9,8),(8,8)]

def get_pos(cell):
    tl = cell[0] * CELL_SIZE,cell[1] * CELL_SIZE
    br = tl[0] + CELL_SIZE,tl[1] + CELL_SIZE
    return tl,br

def get_apple():

    x = random.randint(0,CELLS - 1)
    y = random.randint(0,CELLS - 1)
    while (x,y) in SNAKE_BODY:
            x = random.randint(0,CELLS - 1)
            y = random.randint(0,CELLS - 1)
    return x,y

field = psg.Graph(
        canvas_size=(SIZE,SIZE),
        graph_bottom_left=(0,0),
        graph_top_right=(SIZE,SIZE),
        background_color="black",
        pad=(0,0),
        expand_x=True,
        expand_y=True
        )

APPLE = get_apple()


def create_win():
    
    layout = [[field]]

    return psg.Window(layout=layout,title="SNAKE",element_padding=(0,0),return_keyboard_events=True)

win = create_win()
direction = (0,1)
start_time = time()

while GAME:

    event,values = win.read(timeout = 5)
    if event == psg.WIN_CLOSED:
        break

    if event == "Left:37" and direction != (1,0):
        direction = (-1,0)
    if event == "Up:38" and direction != (0,-1):
        direction = (0,1)
    if event == "Right:39" and direction != (-1,0):
        direction = (1,0)
    if event == "Down:40" and direction != (0,1):
        direction = (0,-1)

    new_time = time() - start_time
    if new_time >= TICK:
        start_time = time()

        if SNAKE_BODY[0] == APPLE:
            APPLE_EATEN = True
            APPLE = get_apple()
            SCORE = SCORE + 10

        new_head = SNAKE_BODY[0][0] + direction[0],SNAKE_BODY[0][1] + direction[1]
        SNAKE_BODY.insert(0,new_head)
        if not APPLE_EATEN:
            SNAKE_BODY.pop()
        APPLE_EATEN = False

        if SNAKE_BODY[0][0] < 0 or SNAKE_BODY[0][0] > CELLS - 1 or SNAKE_BODY[0][1] < 0 or SNAKE_BODY[0][1] > CELLS - 1:
            GAME = False
        if SNAKE_BODY[0] in SNAKE_BODY[1:]:
            GAME = False

        field.DrawRectangle((0,0),(SIZE,SIZE),"black")
        tl,br = get_pos(APPLE)
        field.DrawRectangle(tl,br,"red")



        for i,part in enumerate(SNAKE_BODY):
            tl,br = get_pos(part)
            if i == 0:
                color = "LightGreen"
            else:
                color = "Green"
            field.DrawRectangle(tl,br,color)

psg.popup(f"GAME OVER!\nSCORE:{SCORE}")
win.close()
