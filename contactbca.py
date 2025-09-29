contact = {}
def add_contact(name, phone, email):
    contact[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} Added Successfully.")

def update_contact(name, phone, email):
    if name in contact:
        contact[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} Updated Successfully.")
    else:
        print(f"Contact {name} Not Found.")

def del_contact(name):
     del contact[name]
     print(f"Contact {name} Deleted Successfully.")

def searched_contact(name):
    details = contact[name]
    print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def display_contacts():
    if contact:
        print("Contacts:")
        for name, details in contact.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("No contacts found.")


def main():
    while True:
        print("\nContact Book Nenu")
        print("1. Add Contact")
        print("2. Update Contacts")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Display Contacts")
        print("6. Exit")

        try:
            print("\n")
            choice = int(input("Enter Your Choice (1-6): "))
        except:
            print("Invalid Input. Please Enter A Number Between 1 And 6.")
            continue

        if choice == 1:
            name = input("Enter Your Name: ")
            phone = input("Enter Your Phone Number: ")
            email = input("Enter Your Email: ")
            add_contact(name, phone, email)

        elif choice == 2:
            name = input("Enter The Name Of The Contact To Update: ")
            phone = input("Enter The New Phone Number: ")
            email = input("Enter The New Email: ")
            update_contact(name, phone, email)

        elif choice == 3:
            name = input("Enter The Name Of The Contact To Delete: ")
            if name in contact:
                del_contact(name)
            else:
                print(f"Contact {name} Not Found.")

        elif choice == 4:
            name = input("Enter The Name Of The Contact To Search: ")
            if name in contact:
                searched_contact(name)
            else:
                print(f"Contact {name} Not Found.")
                
        elif choice == 5:
            display_contacts()

        elif choice == 6:
            print("Exiting Contact Book/Application. Goodbye!")
            break


if __name__ == "__main__":
    main()