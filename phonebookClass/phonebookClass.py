question = 1
option = 0

class Phonebook:
    def __init__(self, name):
        self.owner = name
        self.contacts = []
        
    def addContact(self, contact):
        self.contacts.append(contact)
        print("Contact added.")
        
    def removeContact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} removed.")
                return
        
    def seeContacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Contact: {contact.contact}")

    def findContact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"{name}' number is: {contact.contact}.")
                return

class Contact:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

phonebook = Phonebook("My_Phonebook")

while question <= 100:

    option = int(input("\n1 = add number, 2 = remove number, 3 = find number, 4 = see list: "))

    if option == 1:
       
        contact_name = input("\nAdd a phone name: ")
        contact_number  = input("Add a phone number: ")
        
        phonebook.addContact(Contact(contact_name, contact_number))
   
    elif option == 2:
        contact_name = input("\nEnter the name of the contact to remove: ")
        phonebook.removeContact(contact_name)
       
    elif option == 3:
        
        name_to_find = input("\nEnter the name to find the number: ")

        phonebook.findContact(name_to_find)
        
    elif option == 4:
        phonebook.seeContacts()
        
    else:
        print("Invalid option!")
        

   
    



    

