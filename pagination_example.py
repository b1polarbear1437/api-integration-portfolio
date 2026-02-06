import requests

def get_all_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    page = 1
    limit = 5
    all_posts = []

    while True:
        params = {
            "_page": page,
            "_limit": limit
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            if not data:
                break

            all_posts.extend(data)
            page += 1

        except requests.exceptions.RequestException as e:
            print("Pagination API Error:", e)
            break

    print(f"Total posts fetched: {len(all_posts)}")

if __name__ == "__main__":
    get_all_posts()
