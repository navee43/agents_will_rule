




def build_headers(api_key):
    # Validate the API key
   if not api_key or not api_key.strip():
    raise ValueError("API key not found")

   headers ={
        "Authorization" :f"Bearar {api_key}",
        "Content-Type": "Application/json"
    }

    # Create the authorization header
   return headers

    # Create the content type header

    # Return the headers dictionary



try:
    headers = build_headers("")
    print(headers)
except ValueError as error:
    print(error)

