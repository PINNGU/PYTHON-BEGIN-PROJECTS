import PySimpleGUI as psg
from time import time


def create_win(theme):
    psg.theme(theme)

    layout = [
        [psg.Push(),psg.Image("STOPWATCH/pic.png",pad=(0,0),key = "CLOSE",enable_events=True)],
        [psg.VPush()],
        [psg.Text("",key = "TIME",font = "Calibri 22",text_color="#FC3B00")],
        [psg.Button("START",key = "START",border_width=0,size=(6,2),button_color=("#FFFFFF","#FC3B00")),
        psg.Button("LAP",key = "LAP",border_width=0,size=(6,2),button_color=("#FFFFFF","#FC3B00"),visible=False)],
        [],
        [psg.VPush()]

    ]


    return psg.Window(
        "stopwatch",
        layout,
        no_titlebar=True,
        size = (300,300),
        element_justification="center")

win = create_win("black")
counting = False
start = 0
lap_num = 1

while True:

    event,values = win.read(timeout=10)

    if event == "CLOSE":
        break

    if event == "START" and not counting:
        win["START"].update("STOP")
        counting = True
        win["LAP"].update(visible = True)
        start = time()
    elif event == "START" and counting:
        win["START"].update("START")
        counting = False

    if event == "LAP":
        lap = 0


        lap_num = lap_num + 1

    if counting:
        win["TIME"].update(round(time() - start,1))



win.close()
