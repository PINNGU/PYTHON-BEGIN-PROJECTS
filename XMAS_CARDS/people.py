import re

class People():

    comm = []
    names = []

    def make_people(self):
        
        file = open("data.txt","r")
        lines = file.read()
        lines = lines.replace("\n",",")
        lines = lines.split(",")


        for i in range(0,int(len(lines) / 4)):
            temp = {"name":lines[4*i + 0],"cards":int(lines[4*i+1]),"street_name":lines[4*i+2],"street_num":lines[4*i+3]}
            self.names.append(lines[4*i + 0])
            self.comm.append(temp)

        file.close()

    def get_names(self):
        return self.names
    
    def add_person(self,person):
        self.comm.append(person)

    def add_cards(self,person,cards):
        for i in self.comm:
            if i["name"] == person:
                i["cards"] = i["cards"] + cards
                return
    

    def print_people(self):

        self.comm = sorted(self.comm,key = lambda x:x["cards"])
        self.comm = list(reversed(self.comm))
        
        file = open("data_sorted.txt","w")

        for i in self.comm:
            file.write(f"{i['name']} ,Adress: {str(i['street_num'])},{i['street_name']} ... number of cards:{str(i['cards'])}\n")


        file.close()

 


