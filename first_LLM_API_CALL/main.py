from config import load_config, display_config
from llm_client import call_llm, extract_response


def main():

    try:
        config = load_config()

        display_config(config)

        prompt = input("\nAsk anything: ")

        data = call_llm(prompt, config)

        result = extract_response(data)

        print("\n===== AI Assistant =====\n")

        print(result["answer"])

        print("\n===== Token Usage =====")

        print("Model:", result["model"])
        print("Input tokens:", result["prompt_tokens"])
        print("Output tokens:", result["completion_tokens"])
        print("Total tokens:", result["total_tokens"])

    except ValueError as error:
        print(f"Validation error: {error}")

    except RuntimeError as error:
        print(f"API error: {error}")


if __name__ == "__main__":
    main()