class Phone:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


phone_list = []


def create_phone():
    name = input("Enter phone name: ")
    number = input("Enter phone number: ")
    phone = Phone(name, number)
    phone_list.append(phone)
    print(f"Phone '{name}' created successfully!")


def modify_phone():
    name = input("Enter phone name to modify: ")
    for phone in phone_list:
        if phone.name == name:
            phone.number = input("Enter new phone number: ")
            print(f"Phone '{name}' modified successfully!")
            return
    print(f"Phone '{name}' not found!")


def delete_phone():
    name = input("Enter phone name to delete: ")
    for phone in phone_list:
        if phone.name == name:
            phone_list.remove(phone)
            print(f"Phone '{name}' deleted successfully!")
            return
    print(f"Phone '{name}' not found!")


def main():
    while True:
        print("\nPhone Book Menu:")
        print("1. Create a new phone")
        print("2. Modify a phone")
        print("3. Delete a phone")
        print("4. List all phones")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_phone()
        elif choice == "2":
            modify_phone()
        elif choice == "3":
            delete_phone()
        elif choice == "4":
            print("Phone List:")
            for phone in phone_list:
                print(phone)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
