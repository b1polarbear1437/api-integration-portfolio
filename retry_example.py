import requests
import time

def fetch_with_retry(url, retries=3, delay=2):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt} failed:", e)
            time.sleep(delay)

    raise Exception("API failed after multiple retries")

if __name__ == "__main__":
    data = fetch_with_retry("https://jsonplaceholder.typicode.com/users")
    print(f"Fetched {len(data)} records")
