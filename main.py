import requests

from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd
from tqdm import tqdm

import scrapper_modules.GetBooks
import scrapper_modules.GetLinks
import scrapper_modules.LinkBrain
import scrapper_modules.constants


def main():
    scrapping = True
    while scrapping:
        print(scrapper_modules.constants.OPTIONS)
        user_input = input("Entrer votre choix: ")

        if not user_input in [1, 2, 3, 4, 5] and not user_input.isdigit():
            print("Choix invalide")
            continue

        if int(user_input) == 1:
            get_links = scrapper_modules.GetLinks.GetLinks()
            get_links.get_all_links(60)
            get_links.save_to_json()

            links_pages = get_links.links
            for page in tqdm(links_pages):
                req = requests.get(page)
                soup = BeautifulSoup(req.text, 'html.parser')
                get_books = scrapper_modules.GetBooks.GetBooksFromPage()
                get_books.get_books(soup)
                get_books.save_to_json()
            
            all_books = []
            for book in tqdm(get_books.books):
                req = requests.get(book)
                soup = BeautifulSoup(req.text, 'html.parser')
                brain_of_books = scrapper_modules.LinkBrain.LinkBrain(book)
                book_info = brain_of_books.get_all_information(soup)
                all_books.append(book_info)
            data_books = pd.DataFrame(all_books)
            print(data_books)
            data_books.to_csv("all_books.csv")
            
        elif int(user_input) == 2:
            category = input("Entrer la catégorie: ")
            data_books = pd.read_csv("all_books.csv")
            data_books = data_books[data_books["category"] == category]
            data_books.to_csv(category+"_books.csv")

        elif int(user_input) == 3:
            category = input("Entrer la catégorie: ")
            data_books = pd.read_csv("all_books.csv")
            data_books = data_books[data_books["category"] == category]
            category_foler = category+"_all_images"
            p = Path(scrapper_modules.constants.USER_DIR)
            p = p / category_foler
            p.mkdir(parents=True, exist_ok=True)

            for i,row in data_books.iterrows():
                url = row["image_url"]
                response = requests.get(url)
                name_file = row["title"] + ".jpg"
                file_path = p / name_file
                if response.status_code == 200:
                    with open(file_path, 'wb') as file:
                        file.write(response.content)

        elif int(user_input) == 4:
            data_books = pd.read_csv("all_books.csv")
            category_foler = "all_images"
            p = Path(scrapper_modules.constants.USER_DIR)
            p = p / category_foler
            p.mkdir(parents=True, exist_ok=True)
            for i,row in tqdm(data_books.iterrows()):
                url = row["image_url"]
                response = requests.get(url)
                title = row["category"].upper() +"_"+row["title"].replace(" ", "_").replace(":", "_").replace("/", "_").replace(".", "_").replace(",", "_").replace("?", "_")
                name_file = title + "_" + row["category"] + ".jpg"
                file_path = p / name_file
                if response.status_code == 200:
                    with open(file_path, 'wb') as file:
                        file.write(response.content)
        
        elif int(user_input) == 5:
            scrapping = False
            print("Fin du scraping")
            break

if __name__ == "__main__":
    print("Start scraping...")
    main()