



def build_headers(api_key):

    if not api_key or not api_key.strip():
        raise ValueError("API key not found")

    return {
        "Authorization": f"Bearer {api_key.strip()}",
        "Content-Type": "application/json"
    }

   





