import PySimpleGUI as psg
from pathlib import Path


emojis = ["happy",[":D",":P","xD"],
              "sad",[":(",":\\"]
              ]



def create_win(theme):
    psg.theme(theme)
    #psg.set_options(element_padding=0)

    menu  = [
    ["File",["Open","Save","---","Exit"]],
    ["Tools",["Word Count"]],
    ["Add",[emojis]]

    ]

    layout = [
        [psg.Menu(menu)],
        [psg.Text("untitled",key = "FILENAME",font = "Calibri 16")],
        [psg.Multiline(expand_y=True,no_scrollbar=True,pad=(0,0),key = "INPUT")]

    ]

    return psg.Window(layout=layout,title="File Editor",size= (300,400))


win = create_win("reddit")
while True:

    event,values = win.read(timeout=10)

    if event == psg.WIN_CLOSED:
        break
    
    if event == "Open":
        path = psg.popup_get_file('Open',no_window=True)
        if path:
            file = Path(path)
            win["INPUT"].update(file.read_text())
            path = path.split("/")[-1]
            win["FILENAME"].update(path)

    if event == "Save":
        path = psg.popup_get_file("Save As",no_window=True,save_as=True)
        if path:
            file = Path(path)
            file.write_text(values["INPUT"])
            path = path.split("/")[-1]
            win["FILENAME"].update(path)


    if event in emojis[1] + emojis[3]:
        win["INPUT"].update(values["INPUT"] + " " +  event)


    if event == "Word Count":
        text = values["INPUT"]
        text = " ".join(text.split())
        words = text.split(" ")
        psg.popup("Number of words:" ,len(words),words)
    

win.close()
