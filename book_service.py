import json
from selenium.webdriver.common.by import By
from config import SELECTORS, PRODUCTS_FILE, MESSAGES

class BookService:
    def __init__(self, driver):
        self.driver = driver
    
    def _load_products(self, path=PRODUCTS_FILE):
        """Ładuje produkty z pliku JSON"""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def _save_products(self, products, path=PRODUCTS_FILE):
        """Zapisuje produkty do pliku JSON"""
        with open(path, "w", encoding="utf-8") as f:
            json.dump(products, f, ensure_ascii=False, indent=2)
    
    def _get_book_info(self, url: str) -> tuple[str, float] | None:
        """Pobiera informacje o książce z Empiku"""
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        try:
            title_tag = self.driver.find_element(By.CSS_SELECTOR, SELECTORS['title'])
            price_tag = self.driver.find_element(By.CSS_SELECTOR, SELECTORS['price'])
            price_text = price_tag.text.strip().replace("zł", "").replace(",", ".").replace(u"\xa0", "")
            current_price = float(price_text)
            
            return (title_tag.text, current_price)
        except Exception as e:
            print("Nie udało się pobrać książki:", e)
            return None
    
    def _check_price(self, url: str) -> float | None:
        """Sprawdza aktualną cenę książki"""
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        try:
            price_tag = self.driver.find_element(By.CSS_SELECTOR, SELECTORS['price'])
            price_text = price_tag.text.strip().replace("zł", "").replace(",", ".").replace(u"\xa0", "")
            current_price = float(price_text)
            return current_price
        except Exception as e:
            print("Nie udało się pobrać ceny:", e)
            return None
    
    def add_book(self, url):
        """Dodaje książkę do listy obserwowanych"""
        if not url.strip():
            raise ValueError(MESSAGES['url_empty'])
        
        book_info = self._get_book_info(url)
        if book_info is None:
            raise RuntimeError(MESSAGES['fetch_error'])
        
        title, price = book_info
        new_book = {
            "name": title,
            "url": url,
            "lastCheckedPrice": price
        }
        
        books = self._load_products()
        books.append(new_book)
        self._save_products(books)
        
        return title, price
    
    def check_price_updates(self):
        """Sprawdza aktualizacje cen wszystkich książek"""
        books = self._load_products()
        changed_books = []
        
        for book in books:
            new_price = self._check_price(book['url'])
            if new_price is not None:
                prev_price = book.get('lastCheckedPrice')
                
                if prev_price is not None and new_price != prev_price:
                    if new_price < prev_price:
                        changed_books.append({
                            'name': book['name'],
                            'message': f"Cena spadła z: {prev_price} zł na: {new_price} zł",
                            'type': 'decrease'
                        })
                    elif new_price > prev_price:
                        changed_books.append({
                            'name': book['name'],
                            'message': f"Cena wzrosła z: {prev_price} zł na: {new_price} zł",
                            'type': 'increase'
                        })
                
                book['lastCheckedPrice'] = new_price
        
        self._save_products(books)
        return changed_books