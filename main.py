from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from io_utils import load_products, save_products
from price_utils import check_price,get_book



books = load_products()

options = Options()
options.add_argument("--headless")  # Bez otwierania okna przeglądarki
driver = webdriver.Chrome(options=options)

# for book in books:
#     new_price = check_price(driver, book['url'])
#     if new_price is not None:
       
#         prev_price = book.get('lastCheckedPrice')
#         if prev_price is None or new_price < prev_price:
#             print(f"Cena SPADŁA z {prev_price} na {new_price}! Aktualizuję w pliku.")
#             book['lastCheckedPrice'] = new_price
#         else:
#             print(f"Cena nie jest niższa niż poprzednia ({prev_price}).")
#     print()

ulrs = ["https://www.empik.com/cesarstwo-potepionych-wampirze-cesarstwo-tom-2-kristoff-jay,p1476579098,ksiazka-p","https://www.empik.com/onyx-storm-onyksowa-burza-empireum-tom-3-yarros-rebecca,p1560703877,ksiazka-p"]

for url in ulrs:
   book_info = get_book(driver, url)
   if book_info is not None:
        title, price = book_info
        new_book = {
            "name": title,
            "url": url,
            "lastCheckedPrice": price
        }
        books.append(new_book)
        


driver.quit()
save_products(books)