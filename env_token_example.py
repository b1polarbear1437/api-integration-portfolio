import os
import requests

def call_secure_api():
    token = os.getenv("API_TOKEN")

    if not token:
        raise Exception("API_TOKEN environment variable not set")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(
            "https://httpbin.org/bearer",
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        print(response.json())

    except requests.exceptions.RequestException as e:
        print("Secure API Error:", e)

if __name__ == "__main__":
    call_secure_api()
