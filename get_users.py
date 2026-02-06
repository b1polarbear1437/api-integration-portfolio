import requests

def get_users():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        users = response.json()
        for user in users:
            print(f"{user['name']} - {user['email']}")

    except requests.exceptions.RequestException as e:
        print("API Error:", e)

if __name__ == "__main__":
    get_users()
