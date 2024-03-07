phonebook = []
question = 1
option = 0

while question <= 100:
    option = int(input("\n1 = add number, 2 = remove number, 3 = see list: "))

    if option == 1:
        phonebook.append(input("\nAdd a phone number: "))
        
    if option == 2:
        
        index = 0
        
        for number in phonebook:
            
            print(f"press {index} to remove :{number}")
            index += 1

        phonebook.pop(int(input("Wath number you want to remove? ")))
        
    if option == 3:
        print(phonebook)

    question += 1
        
        






