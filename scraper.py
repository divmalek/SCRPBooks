import requests
from bs4 import BeautifulSoup
import csv
print("Welcome to my code! Here's the Python script that detects the yearly top Goodreads books.")
year = input("Entre The Year > ")
page_url = requests.get(f"https://www.goodreads.com/book/popular_by_date/{year}").text
soup = BeautifulSoup(page_url,"lxml")
table = soup.find("div",class_="PopularByDatePage__content").find_all("div",class_="BookListItem__body")
books = []

def main():
    for t in table:
        number = t.find("div",class_="BookListItemRank").text.strip()
        name = t.find("h3",class_="Text Text__title3 Text__umber").text.strip()
        author = t.find("span",class_="ContributorLink__name").text.strip()
        rate = t.find("span",class_="Text Text__body3 Text__semibold Text__body-standard").text.strip()
        full_link = t.find("h3",class_="Text Text__title3 Text__umber").a.get("href").strip()
        books.append({"Book Rank":number,"Book Name":name,"The author":author,"The Rate":rate,"Book Link":full_link})      
    keys = books[0].keys()
    with open("books.csv","w",newline="",encoding='utf-8-sig') as f:
        file_writer = csv.DictWriter(f,keys)
        file_writer.writeheader()
        file_writer.writerows(books)
    print('file created')
main()  