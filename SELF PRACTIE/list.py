my_list = []
print("Menu Are:")
print("1. Insert\n2. Delete\n3. Display\n4. Exit")
while True:
    print("Enter your choice:")
    choice = int(input())
    if choice == 1:
        print("Enter the element to insert:")
        element = int(input())
        my_list.append(element)
        print(f"{element} inserted.")
    elif choice == 2:
        if my_list:
            removed_element = my_list.pop()
            print(f"{removed_element} deleted.")
        else:
            print("List is empty. Nothing to delete.")
    elif choice == 3:
        print("Current List:", my_list)
    elif choice == 4:
        print("Exiting the program.")
        break
