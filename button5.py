from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class Button5(Button):
    def __init__(self, db, **kwargs):
        super().__init__(text="Show Data", **kwargs)
        self.db = db
        self.bind(on_press=self.show_data)

    def show_data(self, instance):
        """ Displays stored product data in a popup. """
        data = self.db.get_stored_products_text()
        popup = Popup(title="Stored Products", content=Label(text=data), size_hint=(None, None), size=(400, 300))
        popup.open()
