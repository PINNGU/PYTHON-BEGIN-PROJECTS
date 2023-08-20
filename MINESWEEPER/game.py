import PySimpleGUI as psg
import numpy as np
from random import randint


class Game():

    dig = True
    flagged = []
    mines = []
    guessed = 0

    def __init__(self,size,mine):
        self.SIZE = size
        self.BOARD = np.full((size,size),'0')
        self.RANGES = []
        self.MINE = mine
        for i in range(0,size):
            for j in range(0,size):
                self.RANGES.append((i,j))

    def make_board(self):
        i = 0
        while i < self.MINE:
            x = randint(0,self.SIZE-1)
            y = randint(0,self.SIZE-1)
            if self.BOARD[x][y] != "X":
                self.BOARD[x][y] = "X"
                self.mines.append([x,y])
                i = i + 1


        for i in range(0,self.SIZE):
            for j in range(0,self.SIZE):
                num = 0
                if  self.BOARD[i][j] != "X":

                    x = i + 1
                    y = j
                    if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                        if self.BOARD[x][y] == "X":
                            num = num + 1

                    x = i + 1
                    y = j + 1
                    if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                        if self.BOARD[x][y] == "X":
                            num = num + 1

                    x = i + 1
                    y = j - 1
                    if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                        if self.BOARD[x][y] == "X":
                            num = num + 1       

                    x = i  - 1
                    y = j
                    if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                        if self.BOARD[x][y] == "X":
                            num = num + 1

                    x = i - 1
                    y = j + 1
                    if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                        if self.BOARD[x][y] == "X":
                            num = num + 1

                    x = i  - 1
                    y = j  - 1
                    if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                        if self.BOARD[x][y] == "X":
                            num = num + 1                
   

                    x = i
                    y = j + 1
                    if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                        if self.BOARD[x][y] == "X":
                            num = num + 1

                    x = i
                    y = j - 1
                    if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                        if self.BOARD[x][y] == "X":
                            num = num + 1        


                    self.BOARD[i][j] = str(num)
    def get_cell_image(self,i,j):

        if self.BOARD[i][j] == "1":
            return "images/MINESWEEPER_1.png"
        if self.BOARD[i][j] == "2":
            return "images/MINESWEEPER_2.png"
        if self.BOARD[i][j] == "3":
            return "images/MINESWEEPER_3.png"
        if self.BOARD[i][j] == "4":
            return "images/MINESWEEPER_4.png"
        if self.BOARD[i][j] == "5":
            return "images/MINESWEEPER_5.png"
        if self.BOARD[i][j] == "6":
            return "images/MINESWEEPER_6.png"
        if self.BOARD[i][j] == "7":
            return "images/MINESWEEPER_7.png"
        if self.BOARD[i][j] == "8":
            return "images/MINESWEEPER_8.png"
        if self.BOARD[i][j] == "0":
            return "images/MINESWEEPER_X.png"
        if self.BOARD[i][j] == "X":
            return "images/MINESWEEPER_M.png"
        
    def get_cell_val(self,i,j):
        pass


    def draw_board(self):

        menu = [
            ["Tool",['Dig','Flag']]
        ]

        lay = [
            [psg.Menu(menu)],
            [[psg.Image("images/MINESWEEPER_0.png",key = (i,j),pad = (0,0),enable_events=True) for j in range(0,self.SIZE)] for i in range(self.SIZE)]
            ]

    
        return psg.Window(title = "MINESWEEPER",layout = lay)
    
    def show_cell(self,i,j,win):
        if self.BOARD[i][j] == 'C':
            return
        elif self.BOARD[i][j] in ["1","2","3","4","5","6","7","8"]:
            win[i,j].update(filename = self.get_cell_image(i,j))
            if [i,j] in self.flagged:
                self.flagged.remove([x,y])
                if [i,j] in self.mines:
                    self.guessed = self.guessed - 1
            return 
        else:
            win[i,j].update(filename = self.get_cell_image(i,j))
            self.BOARD[i][j] = 'C'
            if [i,j] in self.flagged:
                self.flagged.remove([x,y])

            x = i + 1
            y = j
            if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                self.show_cell(x,y,win)

            x = i + 1
            y = j - 1
            if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                self.show_cell(x,y,win)


            x = i + 1
            y = j + 1
            if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                self.show_cell(x,y,win)


            x = i - 1
            y = j
            if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                self.show_cell(x,y,win)
                            
            x = i - 1
            y = j + 1
            if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                self.show_cell(x,y,win)

            x = i - 1
            y = j - 1
            if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                self.show_cell(x,y,win)


            x = i
            y = j + 1
            if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                self.show_cell(x,y,win)


            x = i
            y = j - 1
            if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
                self.show_cell(x,y,win)
   
    def play_board(self):

        win = self.draw_board()

        while True:

            event,values = win.read(timeout=10)

            if event == psg.WIN_CLOSED:
                break

            if self.guessed == self.MINE:
                psg.popup("You WON.")
                break


            if event == "Dig":
                self.dig = True
            elif event == "Flag":
                self.dig = False

            if event in self.RANGES and self.dig:
                x = event[0]
                y = event[1]

                if self.BOARD[x][y] in ["1","2","3","4","5","6","7","8"]:
                    win[event].update(filename = self.get_cell_image(event[0],event[1]))
                    if [x,y] in self.flagged:
                        self.flagged.remove([x,y])
                        if [x,y] in self.mines:
                            self.guessed = self.guessed - 1
                elif self.BOARD[x][y] == "X":
                    win[event].update(filename = self.get_cell_image(x,y))
                    if [x,y] in self.flagged:
                        self.flagged.remove([x,y])
                        if [x,y] in self.mines:
                            self.guessed = self.guessed - 1
                    psg.popup(f"You Exploded!\nYou guessed {self.guessed} mines.")
                    break
                else:
                    self.show_cell(x,y,win)

            if event in self.RANGES and not self.dig:
                x = event[0]
                y = event[1]

                if [x,y] not in self.flagged and len(self.flagged) < self.MINE:
                    self.flagged.append([x,y])
                    win[event].update("images/MINESWEEPER_F.png")
                    if [x,y] in self.mines:
                        self.guessed = self.guessed + 1
            

        
        win.close()

