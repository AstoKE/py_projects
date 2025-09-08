FILE_NAME = "notes.txt"

def show_menu():
    print("\n--- NoteTaking App Menyu ---")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")

def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("Note added successfully!")

def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()
            if content:
                print("\n--- Your Notes ---")
                print(content)
            else:
                print("\nNo notes found")
    except FileNotFoundError:
        print("No notes found")

def delete_notes():
    confirm = input("Are you sure you want to delete all notes? (Yes/no): ")
    if confirm.lower() == "yes":
        with open(FILE_NAME, "w") as file:
            pass
        print("All notes have been deleted")
    else:
        print("Deletion cancelled")

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
         add_note()
    elif choice == "2":
         view_notes()
    elif choice == "3":
         delete_notes()
    elif choice == "4":
         break
    else:
         print("Invalid choice.")
         show_menu()