# contact_manager.py
"""
Robust Contact Manager (student-friendly version)

What this program does:
- Add, find, and delete contacts stored in a dictionary
- Handle bad input without crashing
- Prevent duplicate contacts by raising a custom error
- Print clear messages for the user and return values for tests
"""

from typing import Optional, Dict

# Global contact store (simple for this assignment)
contacts: Dict[str, str] = {}


# ---------- Custom Error ----------
class DuplicateContactError(Exception):
    """Raised when trying to add a contact that already exists."""
    pass


# ---------- Core Functions ----------
def reset_contacts() -> None:
    """Test helper: clear all contacts (used in unit tests)."""
    contacts.clear()


def add_contact(name: str, phone: str) -> bool:
    """
    Add a new contact.

    Returns:
        True if added.
    Raises:
        DuplicateContactError: if the name already exists.
    """
    if name in contacts:
        raise DuplicateContactError(f"Contact '{name}' already exists.")
    contacts[name] = phone
    return True


def find_contact(name: str) -> Optional[str]:
    """
    Get a phone number by name.

    Returns:
        The phone number if found, otherwise None.
    """
    return contacts.get(name)


def delete_contact(name: str) -> bool:
    """
    Remove a contact by name.

    Returns:
        True if deleted, False if the contact was not found.
    """
    if name in contacts:
        del contacts[name]
        return True
    return False


# ---------- CLI Helpers ----------
def print_menu() -> None:
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. Find Contact")
    print("3. Delete Contact")
    print("4. Exit")


def main() -> None:
    """Run the interactive app with safe input handling."""
    while True:
        print_menu()
        choice_raw = input("Enter your choice (1-4): ").strip()

        # Validate that choice is a number 1..4
        try:
            choice = int(choice_raw)
        except ValueError:
            print("Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()
            try:
                add_contact(name, phone)
                print(f"Added {name} to contacts.")
            except DuplicateContactError as e:
                print(e)

        elif choice == 2:
            name = input("Enter name to find: ").strip()
            number = find_contact(name)
            if number is None:
                print("Contact not found.")
            else:
                print(f"{name}: {number}")

        elif choice == 3:
            name = input("Enter name to delete: ").strip()
            if delete_contact(name):
                print(f"Deleted {name}.")
            else:
                print("Contact not found.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()