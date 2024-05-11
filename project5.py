import sys

def initialize_phonebook():
    phonebook = []
    num_contacts = int(input("Please enter the initial number of contacts: "))
    
    for _ in range(num_contacts):
        contact = {}
        contact["name"] = input("Enter name*: ")
        if not contact["name"].strip():
            sys.exit("Name is a mandatory field. Exiting due to blank field...")
        
        contact["number"] = int(input("Enter number*: "))
        
        contact["email"] = input("Enter email address: ") or None
        contact["dob"] = input("Enter date of birth (dd/mm/yy): ") or None
        contact["category"] = input("Enter category (Family/Friends/Work/Others): ") or None
        
        phonebook.append(contact)
    
    return phonebook

def display_menu():
    print("********************************************************************")
    print("\t\t\tContact Book\n")
    print("********************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")

def add_contact(phonebook):
    contact = {}
    contact["name"] = input("Enter name: ")
    contact["number"] = int(input("Enter number: "))
    contact["email"] = input("Enter email address: ")
    contact["dob"] = input("Enter date of birth (dd/mm/yy): ")
    contact["category"] = input("Enter category (Family/Friends/Work/Others): ")
    
    phonebook.append(contact)
    return phonebook

def remove_contact(phonebook):
    query = input("Please enter the name of the contact you wish to remove: ")
    phonebook = [contact for contact in phonebook if contact["name"] != query]
    return phonebook

def delete_all_contacts(phonebook):
    return []

def search_contact(phonebook):
    query = input("Enter search criteria: ")
    results = [contact for contact in phonebook if query.lower() in contact.values()]
    if results:
        for contact in results:
            print(contact)
    else:
        print("Contact not found.")
    
def display_contacts(phonebook):
    if phonebook:
        for contact in phonebook:
            print(contact)
    else:
        print("Phonebook is empty.")

def main():
    print("Welcome to the Smartphone Directory!")
    phonebook = initialize_phonebook()
    
    while True:
        display_menu()
        choice = input("Please enter your choice: ")
        
        if choice == '1':
            phonebook = add_contact(phonebook)
        elif choice == '2':
            phonebook = remove_contact(phonebook)
        elif choice == '3':
            phonebook = delete_all_contacts(phonebook)
        elif choice == '4':
            search_contact(phonebook)
        elif choice == '5':
            display_contacts(phonebook)
        elif choice == '6':
            print("Thank you for using our Smartphone Directory system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
