from config import load_config, display_config
from llm_client import call_llm, extract_response
import time


def main():

    try:
        config = load_config()

        display_config(config)

        prompt = input("\nAsk anything: ")
        start =time.perf_counter()

        data = call_llm(prompt, config)
        end =time.perf_counter()

        duration = end-start
        print(f"Response Time : {duration}" )

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