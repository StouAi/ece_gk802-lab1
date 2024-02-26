import requests
import datetime


if __name__ == "__main__":
    url = input("Enter a URL: ") 

    if not url:
        url = "https://www.google.com"
        print(f"URL was not provided. Default URL: {url}")

    response = requests.get(url) 
    headers = response.headers
    server_header = response.headers['server']

    for header, value in headers.items():
        print(f"{header}: {value}\n")

    cookies = response.cookies
    # print out Cookies
    for cookie in cookies:
        expires = datetime.datetime.fromtimestamp(cookie.expires)
        print(f"cookie name: {cookie.name} ,expiration date: {expires}")

    print(f"Server: {server_header}")

