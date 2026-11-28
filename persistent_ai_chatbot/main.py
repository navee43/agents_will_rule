from config import load_config
from llm_client import call_llm, extract_response
from storage import load_history, save_history, clear_history
import json


def main():

    try:
        config = load_config()

    except ValueError as error:
        print(f"Configuration error: {error}")
        return

    print("==== Persistent AI Assistant ====")
    print("Type 'exit' to exit the chatbot")
    print("Type 'clear' to clear the history")
    print("Type 'history' to view conversation history")

    while True:

        prompt = input("\nYou: ").strip()

        if not prompt:
            print("Enter a valid prompt")
            continue

        if prompt.lower() == "exit":
            print("Application closing...")
            break

        try:

            # Clear conversation history
            if prompt.lower() == "clear":

                confirm = input("Are you sure? (yes/no): ")

                if confirm.strip().lower() == "yes":
                    clear_history()
                    print("History cleared")
                else:
                    print("Operation cancelled")

                continue

            # Display conversation history
            if prompt.lower() == "history":

                history = load_history()

                if not history:
                    print("No conversation history")

                for message in history:
                    print(f"{message['role']}: {message['content']}")

                continue

            # Load previous conversation history
            prev_hist = load_history()

            # Append user message
            prev_hist.append({
                "role": "user",
                "content": prompt
            })

            # Send conversation to LLM
            llm_response = call_llm(prev_hist, config)

            # Extract assistant response
            extracted_res = extract_response(llm_response)

            answer = extracted_res["answer"]

            # Validate response BEFORE saving
            if not answer or not answer.strip():
                raise ValueError("LLM returned an empty response")

            # Append assistant response
            prev_hist.append({
                "role": "assistant",
                "content": answer
            })

            # Save completed conversation
            save_history(prev_hist)

            # Display assistant response
            print(f"\nAssistant: {answer}")

            # Display token usage
            print("\n===== Token Usage =====")
            print(f"Input tokens: {extracted_res['prompt_tokens']}")
            print(f"Output tokens: {extracted_res['completion_tokens']}")
            print(f"Total tokens: {extracted_res['total_tokens']}")

        except json.JSONDecodeError:
            print("Conversation history is corrupted.")

        except ValueError as error:
            print(f"Validation error: {error}")

        except RuntimeError as error:
            print(f"API error: {error}")

        except OSError as error:
            print(f"File operation failed: {error}")


if __name__ == "__main__":
    main()