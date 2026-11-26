from github_client import fetch_profile, extract_profile


def main():

    print("===== GitHub Profile Fetcher =====")

    username = input("Enter GitHub username: ")

    try:
        data = fetch_profile(username)

        profile = extract_profile(data)

        for key, value in profile.items():
            print(f"{key}: {value}")

    except ValueError as error:
        print(f"Invalid input: {error}")

    except RuntimeError as error:
        print(f"API error: {error}")


if __name__ == "__main__":
    main()