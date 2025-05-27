# gui_controller.py
from tkinter import messagebox
from config import MESSAGES

class GuiController:
    def __init__(self, book_service, gui_view):
        self.book_service = book_service
        self.gui_view = gui_view
    
    def handle_add_book(self):
        """Obsługuje dodawanie książki"""
        try:
            url = self.gui_view.get_url()
            title, price = self.book_service.add_book(url)
            messagebox.showinfo(MESSAGES['book_added'], f"Dodano: {title} ({price} zł)")
            self.gui_view.clear_url()
        except ValueError as e:
            messagebox.showwarning("Błąd", str(e))
        except RuntimeError as e:
            messagebox.showerror("Błąd", str(e))
    
    def handle_price_update(self):
        """Obsługuje sprawdzanie aktualizacji cen"""
        try:
            changed_books = self.book_service.check_price_updates()
            
            if changed_books:
                messages = []
                for book in changed_books:
                    messages.append(f"{book['name']}\n{book['message']}")
                result_text = "\n\n".join(messages)
            else:
                result_text = MESSAGES['no_price_changes']
            
            self.gui_view.display_results(result_text)
            
        except Exception as e:
            messagebox.showerror("Błąd", f"{MESSAGES['price_check_error']}: {str(e)}")
    
    def handle_close(self):
        """Obsługuje zamykanie aplikacji"""
        # Tutaj można dodać dodatkową logikę przed zamknięciem
        self.gui_view.close()