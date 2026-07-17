contacts = {}

# Load contacts from file
def load_contacts():
    try:
        file = open("contacts.txt", "r")

        for line in file:
            data = line.strip().split(" : ")

            if len(data) == 2:
                contacts[data[0]] = data[1]

        file.close()

    except FileNotFoundError:
        file = open("contacts.txt", "w")
        file.close()


def add_contact():
    try:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        contacts[name] = phone

        save_contacts()     # Save automatically

        print("Contact Added Successfully!")

    except Exception:
        print("Error while adding contact.")


def view_contacts():
    if len(contacts) == 0:
        print("No Contacts Available.")

    else:
        print("\n----- Contact List -----")

        for name, phone in contacts.items():
            print("Name :", name)
            print("Phone:", phone)
            print()


def search_contact():
    name = input("Enter Name to Search: ")

    if name in contacts:
        print("Phone Number:", contacts[name])
    else:
        print("Contact Not Found.")


def delete_contact():
    name = input("Enter Name to Delete: ")

    if name in contacts:
        del contacts[name]

        save_contacts()     # Save after deleting

        print("Contact Deleted Successfully!")

    else:
        print("Contact Not Found.")


def save_contacts():

    file = open("contacts.txt", "w")

    for name, phone in contacts.items():
        file.write(name + " : " + phone + "\n")

    file.close()

    print("Contacts Saved Successfully!")


# Load contacts when program starts
load_contacts()


while True:

    print("\n====== CONTACT BOOK ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Save Contacts")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        save_contacts()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")