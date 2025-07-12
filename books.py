import requests
from bs4 import BeautifulSoup
import csv

def get_books_from_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"

    if response.status_code != 200:
        raise Exception(f"Erro ao acessar {url}")

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for book in soup.find_all("article", class_="product_pod"):
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text.strip()
        books.append({"title": title, "price": price})

    return books

def save_books_to_csv(book_list, filename="books.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "price"])
        writer.writeheader()
        writer.writerows(book_list)

def main():
    url = "https://books.toscrape.com/"
    books = get_books_from_page(url)
    save_books_to_csv(books)
    print("Create: books.csv")

if __name__ == "__main__":
    main()