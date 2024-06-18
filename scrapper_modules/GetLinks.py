import json

from pathlib import Path
import requests

from constants import USER_DIR, JSON_NAME

class GetLinks:
    nb_page: int = 1
    URL: str = r"https://books.toscrape.com/catalogue/"
    
    def __init__(self):
        print("Init GetLinks")
        self.p = Path(USER_DIR + JSON_NAME)
        if not self.p.exists():
            Path.touch(self.p)
            self.links = []
        else:
            if self.p.stat().st_size == 0:
                self.links = []
            else:
                file_opened = open(self.p, 'r')
                self.links = json.load(file_opened)
                file_opened.close()


    def get_all_links(self, page=1, mode="all", category=""):
        for i in range(self.nb_page,page):
            page_link = "page-" + str(i) + ".html"
            req = requests.get(self.URL + page_link)
            print(req.url)
            if req.status_code == 404:
                print(f"Page {i} n'existe pas. Arrêt du scraping.")
                break
            else:
                if req.url not in self.links:
                    self.links.append(req.url)

    def save_to_json(self):
        with open(self.p, 'w') as f:
            json.dump(self.links, f)
            print("File saved")




