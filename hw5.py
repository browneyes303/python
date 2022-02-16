
import pickle

try:
    with open("phonebook.pickle", "rb") as fh:
        phonebook = pickle.load(fh)
except:
    phonebook = {}

def add_contact(name, phone):
    phonebook[name] = phone
    print(f"Entry stored for {name}")

run_phonebook = True

while run_phonebook:

    selection = int(input(f'''
    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
    '''))

    if selection == 1:
        name = input("Enter name: ")
        if name in phonebook:
            print(f"{name} {phonebook[name]}")
        else:
            print("Contact not found")

    elif selection == 2:

        add_name = input("Enter a name to add: ")
        add_phone = input("Enter phone to add: ")
        add_contact(add_name,add_phone)

    elif selection == 3:

        del_contact = input("Enter a name to delete: ")
        if del_contact in phonebook:
            del phonebook[del_contact]
            print("Contact deleted")
        else:
            print("Contact not found")

    elif selection == 4:

        for name, phonenumber in phonebook.items():
            print(f"Name: {name}, Phone: {phonenumber}")

    elif selection == 5:
        run_phonebook = False
        with open('phonebook.pickle', 'wb') as fh: 
            pickle.dump(phonebook, fh)
