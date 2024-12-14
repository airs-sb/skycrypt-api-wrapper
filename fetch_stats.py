import requests


def fetch_data(username: str) -> dict:
    """
    Fetches the data for a given username from the API.
    """
    url = f"https://sky.shiiyu.moe/api/v2/profile/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error if status is not 200
        return response.json()  # Return the JSON data
    except requests.RequestException as e:
        print(f"Network problem: {e}")
        return {}
    except ValueError:
        print("Couldn't parse response as JSON.")
        return {}