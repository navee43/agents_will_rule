from storage import save_message, read_history, clear_history


def main():
    while True:
        print("\n===== Persistent Conversation Logger =====")
        print("1. Save message")
        print("2. Read history")
        print("3. Clear history")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            role = input("Enter role: ")
            content = input("Enter message: ")

            save_message(role, content)
            print("Message saved successfully")

        elif choice == "2":
            print(read_history())

        elif choice == "3":
            clear_history()
            print("History cleared successfully")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()