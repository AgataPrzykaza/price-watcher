from selenium.webdriver.common.by import By

def check_price(driver, url: str) -> float | None:
    driver.get(url)
    driver.implicitly_wait(10)
    try:
        price_tag = driver.find_element(By.CSS_SELECTOR, 'span[data-ta="price"]')
        price_text = price_tag.text.strip().replace("zł", "").replace(",", ".").replace(u"\xa0", "")
        current_price = float(price_text)
        print(f"Aktualna cena: {current_price} zł")
        return current_price
    except Exception as e:
        print("Nie udało się pobrać ceny:", e)
        return None

#<h1 data-ta="title" class="css-9rngxa-title">Imperium burz. Szklany tron. Tom 5</h1>

def get_book(driver,url:str) -> tuple[str, float] | None:
     driver.get(url)
     driver.implicitly_wait(10)
     try:
        title_tag = driver.find_element(By.CSS_SELECTOR, 'h1[data-ta="title"]')
        print("tyttul: ",title_tag.text)
        price_tag = driver.find_element(By.CSS_SELECTOR,'span[data-ta="price"]')
        price_text = price_tag.text.strip().replace("zł", "").replace(",", ".").replace(u"\xa0", "")
        current_price = float(price_text)

        return (title_tag.text,current_price)
     except Exception as e:
        print("Nie udało się pobrać ksizki:", e)
        return None