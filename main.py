from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from book_service import BookService
from gui_view import GuiView
from gui_controller import GuiController
from config import CHROME_OPTIONS

class BookPriceApp:
    def __init__(self):
        # Inicjalizacja drivera
        options = Options()
        for option in CHROME_OPTIONS:
            options.add_argument(option)
        self.driver = webdriver.Chrome(options=options)
        
        # Inicjalizacja komponentów
        self.book_service = BookService(self.driver)
        self.gui_view = GuiView()
        self.gui_controller = GuiController(self.book_service, self.gui_view)
        
        # Połączenie kontrolera z widokiem
        self.gui_view.set_controller(self.gui_controller)
    
    def run(self):
        """Uruchamia aplikację"""
        try:
            self.gui_view.mainloop()
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Czyści zasoby"""
        if hasattr(self, 'driver'):
            self.driver.quit()

if __name__ == "__main__":
    app = BookPriceApp()
    app.run()