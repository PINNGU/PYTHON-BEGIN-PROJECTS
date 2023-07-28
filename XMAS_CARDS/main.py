#a small project,data and file handling,user enters his name,adress and how many holliday cards he has
#then he chooses how many he wants to send to one of the members of the community(data gathered from a file)
#,after he is done the data is handled and sorted in order,and printed onto a new file
#log file allows for logging errors and misinputs
#the user can sand cards as long as he wants and has them


from people import People
from person import Person


person = Person()
person.new_user()
people = People()
people.make_people()

while(person.sending):
    num_send,who_send = person.send_cards(people.get_names())
    people.add_cards(who_send,num_send)

    x = input("Do you want to send more cards(Y for yes)")
    if(x != "Y" or x != "y"):
        person.sending = False

people.add_person(person.get_person())
people.print_people()


