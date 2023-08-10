import PySimpleGUI as psg


def create_win(theme):
    psg.theme(theme)

    layout = [
        [psg.Push(),psg.Image("pic.png")],
        [psg.VPush()],
        [psg.Text("TIME",key = "TIME",pad = (7,7))],
        [psg.Button("START",key = "START",border_width=0,size=(8,2),button_color=("#FFFFFF","#FC3B00"))],
        [psg.VPush()]

    ]


    return psg.Window("stopwatch",layout,size = (300,300),element_justification="center")

win = create_win("black")

while True:

    event,values = win.read()

    if event == psg.WIN_CLOSED:
        break


win.close()
