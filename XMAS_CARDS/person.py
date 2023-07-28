import logging
logging.basicConfig(filename = "log.log",filemode = "w",level = logging.DEBUG,
                    format = "%(levelname)s - %(message)s - %(asctime)s - m:%(module)s,line: %(lineno)s ")

class Person():

    name = ""
    street_name = ""
    street_num = 0
    cards_num = 0
    sending = True

    def handle_input1(self):
        word = input()
        word = word.strip()
        word = word.title()
        return word
    
    def handle_input2(self):
        while(True):
            try:
                num = int(input())
                if(num < 0):
                    continue
            except:  
                print("Wrong input.")
                logging.exception("wrong input.")
                continue
            else:
                break

        return num


    def new_user(self):

        print("Welcome,merry christmas!\nPlease enter your name:")
        
        self.name = self.handle_input1()

        print("Now,enter your street name:")
        self.street_name = self.handle_input1()

        print("And your street number:(enter only a positive number):")
        self.street_num = self.handle_input2()

        print("How many cards do you have(enter only a positive number):")
        self.cards_num = self.handle_input2()


    def send_cards(self,names):

        while(True):
            try:
                to_send = int(input("How many cards do you wish to send?"))
                if to_send == 0:
                    break
            except:  
                print("Wrong input.")
                logging.exception("wrong input.")
                continue
            else:
                if(to_send > self.cards_num):
                    print("You dont have that many cards.")
                    logging.exception("no cards.")
                    continue
                else:
                    self.cards_num = self.cards_num - to_send
                    break
        
        who_send = None
        while(who_send == None):
            print("Who to send it to?")
            who_send = self.handle_input1()
            if(who_send not in names):
                print("Non existant person.")
                logging.exception("called non-existant")
                who_send = None
                continue


        print("Cards sent!\n")
            
        return to_send,who_send

    def get_person(self):
        return {"name":self.name,"cards":self.cards_num,"street_name":self.street_name,"street_num":self.street_num}




