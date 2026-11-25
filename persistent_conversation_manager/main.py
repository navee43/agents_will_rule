import json

from storage import (
    add_message,
    load_history,
    get_user_messages,
    get_recent_messages,
    count_messages,
    clear_history
)


def main():
    while True:
        print("\n===== AI Conversation Manager =====")
        print("1. Add message")
        print("2. Display history")
        print("3. Get user messages")
        print("4. Get recent messages")
        print("5. Count messages")
        print("6. Clear history")
        print("7. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                role = input("Enter role: ")
                content = input("Enter message: ")

                add_message(role, content)
                print("Message saved successfully")

            elif choice == "2":
                messages = load_history()

                if not messages:
                    print("No conversation history available.")

                for message in messages:
                    print(f"{message['role']}: {message['content']}")

            elif choice == "3":
                print(get_user_messages())

            elif choice == "4":
                n = int(input("How many recent messages do you want? "))
                print(get_recent_messages(n))

            elif choice == "5":
                print(f"Total messages: {count_messages()}")

            elif choice == "6":
                confirm = input("Are you sure? (yes/no): ")

                if confirm.strip().lower() == "yes":
                    clear_history()
                    print("History cleared successfully")
                else:
                    print("Operation cancelled")

            elif choice == "7":
                print("Exiting program...")
                break

            else:
                print("Invalid choice")

        except json.JSONDecodeError:
            print("Conversation history is corrupted.")

        except ValueError as error:
            print(f"Invalid input or data: {error}")

        except OSError as error:
            print(f"File operation failed: {error}")


if __name__ == "__main__":
    main()