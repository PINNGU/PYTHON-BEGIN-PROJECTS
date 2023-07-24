from word import Word

wr = Word()

wr.get_words_from_file()

x = input("Type 1 to start if you are ready,any other number to quit:")

if(x != "1"):
    quit()

wr.get_random_word()
wr.game()


#dedicated to A