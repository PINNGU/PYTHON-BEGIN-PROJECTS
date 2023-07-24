
igra_matrica = [["-","*","-"],["*",".","*"],["-","*","-"]] ## Razliciti simboli praznog polja(-,*,.) zbog preduslova jednog if dalje u zadatku,ovo je jednostavnije samo lol

def dobrodosli():    #meni pocetni
    x = "0"
    while(x != "1" and x != "2"):
        print("Dobrodosli u igru IKS-OKS.Izaberite 1 ili 2 igraca:")
        x = input()
        if x == "1":
            return False
        elif x == "2":
            return True
        else:
            continue
        

def draw():  #CRTANJE MATRICE IGRE IKS OKS

    print("        0       1       2\n    -------------------------")
    y = 0
    for red in igra_matrica:
        print(y,"  |"," ",red[0],"  |"," ",red[1],"  |"," ",red[2],"  |") 
        print("    -------------------------")
        y = y + 1
    
def game_over():  #PROVERA LOGIKE IGRE,DA LI POSTOJI 3 SIMBOLA ZAREDOM 
    for n in igra_matrica:
        if n[0] == n[1] == n[2] and n[0]:
            return True
        
    for i in range(0,3):
        if igra_matrica[0][i] == igra_matrica[1][i] == igra_matrica[2][i]: 
            return True
    
    if igra_matrica[0][0] == igra_matrica [1][1] == igra_matrica[2][2]:
        return True
    
    if igra_matrica[0][2] == igra_matrica[1][1] == igra_matrica[2][0]:
        return True
    
    return False
    


def dva_igraca():
    turn = 0
    while turn < 9:
        p_red = 4
        p_kolona = 4
        draw()
        while(p_red != 0 and p_red != 1 and p_red != 2):
            print("Izaberi red:")
            p_red = int(input())

        while(p_kolona != 0 and p_kolona != 1 and p_kolona != 2):
            print("Izaberi kolonu:") 
            p_kolona = int(input())

        
        if(igra_matrica[p_red][p_kolona] != "X" and igra_matrica[p_red][p_kolona] != "O" and  turn % 2 == 0):
            igra_matrica[p_red][p_kolona] = "X"
        elif(igra_matrica[p_red][p_kolona] != "O" and igra_matrica[p_red][p_kolona] != "X" and  turn % 2 == 1):
            igra_matrica[p_red][p_kolona] = "O"
        else:
            print("------Ne mozete to igrati.--------")
            print("------Pokusajte ponovo.-----------")
            continue

        turn = turn + 1
        if(game_over()):
                draw()
                print("\n!!!!!!GOTOVA IGRA!!!!!!!")
                return
        continue 
      
def bot_turn():  #bot pametno razmislja gde da stavi simbol 'O',uvijek ce staviti u centar ako je prazno polje(najjace polje u igri,omogucava plus 2 kombinacije za 
    if(igra_matrica[1][1] != "X" and igra_matrica[1][1] != "O"):    #pobedu - dijagonale),ako ne stavi u centar prati algoritam POBEDA->GUBITAK->RANDOM
        igra_matrica[1][1] = "O"
        return
    else:
        for i in range(0,3):
            for j in range(0,3):
                if(igra_matrica[i][j] != "X" and igra_matrica[i][j] != "O"):
                    temp = igra_matrica[i][j]
                    igra_matrica[i][j] = "O"

                    if(game_over()):  # AKO CE BOT DA POBIJEDI,OVIM KORAKOM,URADI TAJ KORAK,I POBIJEDI
                        igra_matrica[i][j] = "O"  
                        print(i," ",j,igra_matrica[i][j])
                        return
                    else:
                        igra_matrica[i][j] = temp  # AKO NIJEDAN NIJE OD TIH SLUCAJA,VRATI NA NORMALNO POLJE,IZADJI IZ TESTIRANJA,STAVI NA RANDOM(REDOM) SLOBODNU POZICIJU
                        print(i," ",j,igra_matrica[i][j])
                        continue

        for i in range(0,3):  # ovo je kopija prethodne funkcije,samo sto se proverava gubitak(X),ovako resavam jer ako stavim sve u jedan loop,
            for j in range(0,3):  # i ne nadje mogucnost pobjede,odmah ce staviti dodge gubitka,iako postoji mogucnost da pobijedi negde u narednim
                if(igra_matrica[i][j] != "X" and igra_matrica[i][j] != "O"):    #iteracijama,zbog toga su 2 loopa
                    temp = igra_matrica[i][j]
                    igra_matrica[i][j] = "X"

                    if(game_over()):  # AKO CE BOT DA IZGUBI OVIM KORAKOM,PREDUHITI IGRACA I NE DOZVOLI GUBITAK
                        igra_matrica[i][j] = "O"  
                        print(i," ",j,igra_matrica[i][j])
                        return
                    else:
                        igra_matrica[i][j] = temp  # AKO NIJEDAN NIJE OD TIH SLUCAJA,VRATI NA NORMALNO POLJE,IZADJI IZ TESTIRANJA,STAVI NA RANDOM(REDOM) SLOBODNU POZICIJU
                        print(i," ",j,igra_matrica[i][j])
                        continue

        for i in range(0,3):    
            for j in range(0,3):  #### NORMALNA SLOBODNA POZICIJA,BEZ PREDUSLOVA I POKUSAJA
                if(igra_matrica[i][j] != "X" and igra_matrica[i][j] != "O"):   
                        igra_matrica[i][j] = "O"
                        return


    

def jedan_igrac():
    turn = 0
    while turn < 5:  #5 turnova igraca,umesto 9 koliko ima polja
        p_red = 4
        p_kolona = 4
        draw()
        while(p_red != 0 and p_red != 1 and p_red != 2):   #provera da li je dobar unos
            print("Izaberi red:")
            p_red = int(input())

        while(p_kolona != 0 and p_kolona != 1 and p_kolona != 2): # same
            print("Izaberi kolonu:") 
            p_kolona = int(input())

        
        if(igra_matrica[p_red][p_kolona] != "X" and igra_matrica[p_red][p_kolona] != "O"):
            igra_matrica[p_red][p_kolona] = "X"
        else:  # ako je pokusaj da stavi na vec popunjeno
            print("------Ne mozete to igrati.--------")  
            print("------Pokusajte ponovo.-----------")
            continue

        bot_turn()  # bot igra
        turn = turn + 1 

        if(game_over()):
                draw()
                print("\n!!!!!!GOTOVA IGRA!!!!!!!")
                quit()
        continue 




if(dobrodosli()): #biranje 
    dva_igraca()
else:
    jedan_igrac()
    
draw() #finalno crtanje,radi lepote programa
print("\n!!!!!!GOTOVA IGRA!!!!!!!")  # ako je draw,ispisi da je gotovo
