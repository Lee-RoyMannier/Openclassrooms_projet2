import json

from pathlib import Path
import requests

from constants import USER_DIR, LINKS_BOOKS, HREF_FULL_LINK

class GetBooksFromPage:
    def __init__(self):        
        self.p = Path(USER_DIR + LINKS_BOOKS)
        print(self.p)
        if not self.p.exists():
            Path.touch(self.p)
            self.books = []
        else:
            if self.p.stat().st_size == 0:
                self.books = []
            else:
                with open(self.p, 'r') as file_opened:
                    self.books = json.load(file_opened)

    def get_books(self, soup):
        get_a = soup.find_all('div', class_="image_container")
        for a in get_a:
            href = HREF_FULL_LINK + "catalogue/" + a.find('a')['href']
            if href not in self.books:
                self.books.append(href)  

    def save_to_json(self):
        with open(self.p, 'w') as f:
            json.dump(self.books, f)
            print("File saved")      