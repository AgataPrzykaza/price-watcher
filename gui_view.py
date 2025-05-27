import tkinter as tk
from config import WINDOW_TITLE, ENTRY_WIDTH, TEXT_BOX_HEIGHT, TEXT_BOX_WIDTH

class GuiView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(WINDOW_TITLE)
        self._setup_ui()
        self.controller = None
    
    def set_controller(self, controller):
        """Ustawia kontroler dla widoku"""
        self.controller = controller
        self._bind_events()
    
    def _setup_ui(self):
        """Konfiguruje interfejs użytkownika"""
        frame = tk.Frame(self, padx=20, pady=20)
        frame.pack()
        
        tk.Label(frame, text="Wklej link do książki z Empiku:").pack(pady=(0, 8))
        
        self.url_entry = tk.Entry(frame, width=ENTRY_WIDTH)
        self.url_entry.pack(pady=(0, 8))
        
        self.add_button = tk.Button(frame, text="Dodaj książkę")
        self.add_button.pack()
        
        self.update_button = tk.Button(frame, text="Update cen")
        self.update_button.pack(pady=(8, 0))
        
        self.result_box = tk.Text(frame, height=TEXT_BOX_HEIGHT, width=TEXT_BOX_WIDTH, state=tk.DISABLED)
        self.result_box.pack(pady=(12, 0))
    
    def _bind_events(self):
        """Wiąże wydarzenia z metodami kontrolera"""
        if self.controller:
            self.add_button.config(command=self.controller.handle_add_book)
            self.update_button.config(command=self.controller.handle_price_update)
            self.protocol("WM_DELETE_WINDOW", self.controller.handle_close)
    
    def get_url(self):
        """Pobiera URL z pola tekstowego"""
        return self.url_entry.get().strip()
    
    def clear_url(self):
        """Czyści pole URL"""
        self.url_entry.delete(0, tk.END)
    
    def display_results(self, text):
        """Wyświetla wyniki w polu tekstowym"""
        self.result_box.config(state=tk.NORMAL)
        self.result_box.delete("1.0", tk.END)
        self.result_box.insert(tk.END, text)
        self.result_box.config(state=tk.DISABLED)
    
    def close(self):
        """Zamyka aplikację"""
        self.destroy()