# Books toscrap – Python Project

This is a Python project built during my learning process.  
It performs web scraping on an online bookstore to extract book titles and prices, saving them into a CSV file.

---

## What does the program do?

* Sends an HTTP request to the main page of books.toscrape.com  
* Parses the HTML content using BeautifulSoup  
* Extracts each book's title and price from the page  
* Stores the data in a structured list of dictionaries  
* Writes the data into a CSV file named `books.csv`  
* Prints a success message when the CSV is created  

---

## Technologies used

* Python 3  
* HTTP requests with `requests`  
* HTML parsing with `BeautifulSoup` (bs4)  
* Data export using the `csv` module  
* Headers to simulate browser access  
* Function separation for modular design  
* UTF-8 encoding for international characters  

---

## Status

MVP complete – currently handles scraping from the homepage only