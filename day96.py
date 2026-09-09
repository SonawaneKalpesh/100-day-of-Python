import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    print("===== API RESPONSE =====")
    print("User ID:", data["userId"])
    print("Post ID:", data["id"])
    print("Title:", data["title"])
    print("Body:", data["body"])

except requests.exceptions.RequestException as error:
    print("API request failed:", error)