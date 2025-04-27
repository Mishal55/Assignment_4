
# Create an empty dictionary to store phonebook information
phonebook = {}

# Function to add a contact to the phonebook
def add_contact(name, phone_number):
    phonebook[name] = phone_number
    print(f"Contact {name} added with phone number {phone_number}.")

# Function to search for a contact's phone number
def search_contact(name):
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}.")
    else:
        print(f"{name} not found in the phonebook.")

# Function to display all contacts in the phonebook
def display_contacts():
    if phonebook:
        print("Phonebook contacts:")
        for name, phone_number in phonebook.items():
            print(f"{name}: {phone_number}")
    else:
        print("The phonebook is empty.")

# Main program loop
while True:
    print("\nPhonebook Options:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")

    # Ask for user choice
    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        # Add a new contact
        name = input("Enter the contact's name: ")
        phone_number = input(f"Enter {name}'s phone number: ")
        add_contact(name, phone_number)
    elif choice == "2":
        # Search for a contact
        name = input("Enter the name to search for: ")
        search_contact(name)
    elif choice == "3":
        # Display all contacts
        display_contacts()
    elif choice == "4":
        print("Exiting the phonebook program.")
        break
    else:
        print("Invalid option. Please choose again.")
