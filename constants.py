import os

USER_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_NAME = "/links.json"
LINKS_BOOKS = "/books.json"
LINKS_CATEGORY = "/category.json"
HREF_FULL_LINK = "https://books.toscrape.com/"
LINK = 'https://books.toscrape.com/catalogue/category/books_1/index.html'

OPTIONS = """
    Bienvenue sur le site de scraping de livres,
    Vous avez le choix entre les options suivantes:
    1 - Récupérer toutes les informations du site de toutes les categories
    2 - Récupérer les informations d'une catégorie (Veuillez choisir cette option apres avec recuperer toutes les informations du site)
    3 - Récupérer les images de livres d'une catégorie
    4 - Récupérer toutes les images de livres (Veuillez choisir cette option en dernier)
    5 - Quitter
"""
