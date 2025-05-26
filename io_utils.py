import json

def load_products(path="products.json"):
    with open(path,"r",encoding="utf-8") as f:
        return json.load(f)

def save_products(products, path="products.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    