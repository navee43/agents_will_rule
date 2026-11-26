import requests


def fetch_profile(username):
    if not username.strip():
        raise ValueError("Enter a valid username.")

    try:
        url = f"https://api.github.com/users/{username.strip()}"

        response = requests.get(url, timeout=10)

        print(response.status_code)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        raise RuntimeError("API request timed out.")

    except requests.exceptions.ConnectionError:
        raise RuntimeError("Could not connect to the API.")

    except requests.exceptions.HTTPError as error:
        raise RuntimeError(f"HTTP error: {error}")

    except requests.exceptions.JSONDecodeError:
        raise RuntimeError("API returned invalid JSON.")

    except requests.exceptions.RequestException as error:
        raise RuntimeError(f"Request failed: {error}")



def extract_profile(res):

    data = {
        "Username": res.get("login"),
        "Name": res.get("name") or "Not available",
        "Biography": res.get("bio") or "Not available",
        "Location": res.get("location") or "Not available",
        "Followers": res.get("followers", 0),
        "Following": res.get("following", 0),
        "Public Repositories": res.get("public_repos", 0),
        "Profile URL": res.get("html_url")
    }

    return data


headers={
    "Authorization" :f"Bearer{API_KEYS}",
    "Content-Type" : "Application/json"
}



    # Extract required information
    # Return a new dictionary
    