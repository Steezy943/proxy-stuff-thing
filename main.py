import requests

PROXIES = {
    'http': 'http://162.4.229.233:8080',
    'https': 'http://162.4.229.233:8080',
}

def search_with_proxy(url):
    try:
        print(f"Connecting to {url} via proxy...")
        response = requests.get(url, proxies=PROXIES, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Test target website
    test_url = 'https://httpbin.org'
    print(search_with_proxy(test_url))
