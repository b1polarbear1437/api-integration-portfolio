import requests

def call_authenticated_api():
    url = "https://httpbin.org/bearer"

    headers = {
        "Authorization": "Bearer sample-token"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print(response.json())

    except requests.exceptions.RequestException as e:
        print("Auth API Error:", e)

if __name__ == "__main__":
    call_authenticated_api()
