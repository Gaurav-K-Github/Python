def display_menu():#outlay
    print("Contact Book Menu:")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Quit")

def display_contacts(contacts):#find and display
    print("\nContacts:")
    if not contacts:
        print("No contacts found.")
    else:
        for name, (phone, email) in contacts.items():
            print(f"{name}: {phone}, {email}")
            
def add_contact(contacts):#new contact and update
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contacts[name] = (phone, email)
    print(f"\nContact '{name}' added successfully!")

def search_contact(contacts):
    name = input("Enter name to search: ")
    contact = contacts.get(name)
    if contact:
        print(f"\nContact Details for {name}:")
        print(f"Phone: {contact[0]}")
        print(f"Email: {contact[1]}")
    else:
        print(f"\nContact '{name}' not found.")

def main():
    contacts = {}

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
main()            
