shopping_list = []

def show_menu():
    print("\n---Shopping List Menu ---")
    print("1. View the shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Clear List")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n--- Shopping List ---")
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            for index, item in enumerate(shopping_list):
                print(f"{index + 1}. {item}")
    elif choice == "2":
        new_item = input("Enter the name of item you want to add:")
        shopping_list.append(new_item)
        print(f"{new_item} has been added to the shopping list.")
    elif choice == "3":
        remove_item = input("Enter the name of item you want to remove:")
        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
            print(f"{remove_item} has been removed to the shopping list.")
        else:
            print(f"{remove_item} is not in the shopping list.")
    elif choice == "4":
        confirm = input("Do you really want to clear list?(Yes/No) --> ")
        if confirm == "Yes":
            shopping_list.clear()
            print("List is successfully cleared!")
        elif confirm == "No":
            show_menu()
    elif choice == "5":
        print("Byeee")
        break
    else:
        print("You entered invalid input!(1-5)")
        show_menu()