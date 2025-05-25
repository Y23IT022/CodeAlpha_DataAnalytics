import requests
from bs4 import BeautifulSoup

try:
    url = 'http://books.toscrape.com/'
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('h3')
        if books:
            for i, book in enumerate(books[:10], 1):
                title = book.a['title']
                print(f"{i}. {title}")
        else:
            print("No book titles found.")
    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
