phonebook = {"Marcos": "22233"}

print("Welcome to the phonebook\n\n")
option = int(input("Options:\nAdd phone - 1\nSearch Phone - 2\nDelete Phone - 3\n\nEnter option: "))

if option == 1:
    name = input("Enter the person name: ")
    phone = input("Enter the person phone (only numbers): ")
    phonebook[name] = phone
    print("Phonebook: " + str(phonebook))
elif option == 3:
    print(phonebook)
    name = input("Who do you want to delete: ")
    phonebook.pop(name)
    print("New phonebook: " + str(phonebook))
elif option == 2:
    name = input("Person name to search: ")
    for person in phonebook:
        if name == person:
            print("\nPhone: " + str(phonebook[name]))
