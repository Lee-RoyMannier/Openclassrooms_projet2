from scrapper_modules.constants import HREF_FULL_LINK

class LinkBrain:
    STARS_TRANSFORMATION = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    def __init__(self, product_page_url):
        print("Init LinkBrain")
        self.product_page_url = product_page_url
        self.upc = ""
        self.title = ""
        self.price_including_tax = ""
        self.price_excluding_tax = ""
        self.number_available = ""
        self.product_description = ""
        self.category = ""
        self.review_rating = ""
        self.image_url = ""

    def get_upc(self, soup):
        table = soup.find_all('table')
        upc = soup.find('th', text='UPC').find_next_sibling('td').text
        self.upc = upc

    def get_title(self, soup):
        title = soup.find('h1').text
        self.title = title
    
    def get_price_including_tax(self, soup):
        price_including_tax = soup.find('th', text='Price (incl. tax)').find_next_sibling('td').text
        self.price_including_tax = price_including_tax.strip("Â£")
    
    def get_price_excluding_tax(self, soup):
        price_excluding_tax = soup.find('th', text='Price (excl. tax)').find_next_sibling('td').text
        self.price_excluding_tax = price_excluding_tax.strip('Â£')
    
    def get_number_available(self, soup):
        number_available = soup.find('th', text='Availability').find_next_sibling('td').text
        number_available = number_available.strip('In stock (').strip(' available)')
        self.number_available = number_available

    def get_product_description(self, soup):
        product_description = soup.find('meta', attrs={'name': 'description'})['content']
        self.product_description = product_description

    def get_category(self, soup):
        category = soup.find('ul', class_='breadcrumb').find_all('a')[2].text
        self.category = category
    
    def get_review_rating(self, soup):
        review_rating = soup.find('p', class_='star-rating')['class'][1]
        review = self.STARS_TRANSFORMATION.get(review_rating, 0)
        
    def get_image_url(self, soup):
        image_url_src = soup.find('div', class_='item active').find('img')['src']
        self.image_url = HREF_FULL_LINK + image_url_src.strip("../../")

    def get_all_information(self, soup):
        self.get_upc(soup)
        self.get_title(soup)
        self.get_price_including_tax(soup)
        self.get_price_excluding_tax(soup)
        self.get_number_available(soup)
        self.get_product_description(soup)
        self.get_category(soup)
        self.get_review_rating(soup)
        self.get_image_url(soup)
        book_information = {
            "product_page_url": self.product_page_url,
            "universal_ product_code (upc)": self.upc,
            "title": self.title,
            "price_including_tax": self.price_including_tax,
            "price_excluding_tax": self.price_excluding_tax,
            "number_available": self.number_available,
            "product_description": self.product_description,
            "category": self.category,
            "review_rating": self.review_rating,
            "image_url": self.image_url
        }    
        return book_information
