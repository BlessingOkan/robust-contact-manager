# buggy_contacts.py

contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added {name} to contacts.")

def find_contact(name):
    print(contacts[name])

def delete_contact(name):
    del contacts[name]
    print(f"Deleted {name}.")

def main():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter name to find: ")
            find_contact(name)
        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()