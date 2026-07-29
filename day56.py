phonebook = {}

while True:
    print("\n--- PHONEBOOK ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        phonebook[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in phonebook:
            print("Phone number:", phonebook[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to update: ")

        if name in phonebook:
            phone = input("Enter new phone number: ")
            phonebook[name] = phone
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in phonebook:
            del phonebook[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        if phonebook:
            print("\n--- All Contacts ---")

            for name, phone in phonebook.items():
                print(name, ":", phone)
        else:
            print("Phonebook is empty.")

    elif choice == "6":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice.")