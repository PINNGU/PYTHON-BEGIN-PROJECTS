import PySimpleGUI as psg

ans = 0
output = ''
calculated = False


def create_win(theme,size,menu):
    psg.theme(theme)
    psg.set_options(font = "Candara 18")

    layout = [
        [psg.Push(),psg.Image("cross.png",pad = 0,enable_events=True,key = "CLOSE")],
        [psg.Text("0",
                  pad = (12,20),
                  expand_x=True,
                  justification="right",
                  font = "Aharoni 24",
                  right_click_menu = menu,
                  key = "OUTPUT"
                  )],
        [psg.Button("Clear",size=size,expand_x=True,border_width=0,button_color="#FC7703"),psg.Button("Ans",size=size,expand_x=True,border_width=0,button_color="#FC7703"),psg.Button("+",size=size,border_width=0,button_color="#FC7703")],
        [psg.Button("9",size=size,border_width=0,button_color="#FC7703"),psg.Button("8",size=size,border_width=0,button_color="#FC7703"),psg.Button("7",size=size,border_width=0,button_color="#FC7703"),psg.Button("-",size=size,border_width=0,button_color="#FC7703")],
        [psg.Button("6",size=size,border_width=0,button_color="#FC7703"),psg.Button("5",size=size,border_width=0,button_color="#FC7703"),psg.Button("4",size=size,border_width=0,button_color="#FC7703"),psg.Button("*",size=size,border_width=0,button_color="#FC7703")],
        [psg.Button("3",size=size,border_width=0,button_color="#FC7703"),psg.Button("2",size=size,border_width=0,button_color="#FC7703"),psg.Button("1",size=size,border_width=0,button_color="#FC7703"),psg.Button("/",size=size,border_width=0,button_color="#FC7703")],
        [psg.Button("0",size=size,expand_x=True,border_width=0,button_color="#FC7703"),psg.Button("=",size=size,border_width=0,button_color="#FC7703"),psg.Button(".",size=size,border_width=0,button_color="#FC7703")]
    ]
    
    return psg.Window("Calculator",layout,no_titlebar=True)

themes = ['menu',["dark","reddit","LightGrey6","HotDogStand"]]

window = create_win("dark",(6,2),themes)

while True:

    event,values = window.read()

    if event == "CLOSE":
        break

    if event in themes[1]:
        window.close()
        window = create_win(event,(6,2),themes)

    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        if len(output) < 14:
            if calculated:
                output = ''
            calculated = False
            output = output + event
            window["OUTPUT"].update(output)

    if event in ['-','+','*','/']:
        if len(output) < 14 and len(output) > 0:
            output = output + event
            window["OUTPUT"].update(output)
            calculated = False

    if event in "Ans":
        if ans != 0:
            output = output + str(ans)
            window["OUTPUT"].update(output)

    if event in "=":
        output = ''.join(output)
        output = eval(output)
        window["OUTPUT"].update(output)
        ans = output
        calculated = True
        output = str(output)

    if event in "Clear":
        window["OUTPUT"].update("0")
        output = ''

window.close()