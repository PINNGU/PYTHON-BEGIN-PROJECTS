#imports words from a text file

from random import randint

class Word():

    showed = "_ _ _ _ _" # 0 2 4 6 8 -> letters 12345
    game_over = False
    turns = 0
        
    def get_words_from_file(self):
        try:
            f = open("words.txt","r")
            content = f.read()
            self.content = content.split("\n")
            print("All words read.Game is ready.")
            f.close()
            
        except:
            print("file doesnt exist.")
            quit()

    def get_random_word(self):
        
        r_n = randint(0,len(self.content))
        self.result = (self.content[r_n])

    def game(self):
        guess = " "
        while(not self.game_over):

            while(len(guess) != 5):
                guess = input("Type a 5 letter word:\n")
                guess = guess.replace(" ","")
                guess = guess.lower()
                

            hint = "\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C"
            guess = list(guess)

            for i in range(0,5):
                if guess[i] == self.result[i]:
                    guess[i] = f"\033[1;32;40m{guess[i].upper()}\033[0m"
                    #hint[i] = "\U00002705"
                elif guess[i] in self.result:
                    guess[i] = f"\033[1;33;40m{guess[i].upper()}\033[0m"
                    #hint[i] = "\U0001F7E1"
                else:
                    guess[i] = f"\033[1;31;40m{guess[i].upper()}\033[0m"
                    continue

            for i in range(0,5): 
                print(guess[i]," ",end="")    

            print("\n") 

            #print("\n",hint,"\n")

            if(guess == self.result):
                print("\nGreat job!!!\n")
                self.game_over = True
            elif(self.turns >= 5):
                print("\nNo more turns left...")
                print("The resulting word is: ",self.result)
                self.game_over = True
            else:
                self.turns = self.turns + 1
                print(f"Turns left: {6-self.turns}")
                guess = ""
                continue

        return

            
            
            


            



