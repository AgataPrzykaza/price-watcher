# Selenium settings
CHROME_OPTIONS = [
    "--headless",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]

# CSS selectors dla Empiku
SELECTORS = {
    'title': 'h1[data-ta="title"]',
    'price': 'span[data-ta="price"]'
}

# File paths
PRODUCTS_FILE = "products.json"

# GUI settings
WINDOW_TITLE = "Dodaj książkę do obserwowanych (Empik)"
ENTRY_WIDTH = 60
TEXT_BOX_HEIGHT = 10
TEXT_BOX_WIDTH = 70

# Messages
MESSAGES = {
    'url_empty': "Wklej adres URL książki z Empiku!",
    'book_added': "Dodano",
    'fetch_error': "Nie udało się pobrać danych o książce",
    'no_price_changes': "Brak zmian w cenach książek.",
    'price_check_error': "Wystąpił błąd podczas sprawdzania cen"
}