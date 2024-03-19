import requests


def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def add(a, b):
    return a + b
