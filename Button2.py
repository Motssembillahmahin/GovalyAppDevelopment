from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class Button2(Button):
    def __init__(self, **kwargs):
        super().__init__(text="Store Data", **kwargs)
        self.db = None
        self.update_callback = None
        self.bind(on_press=self.show_popup)

    def set_db_connection(self, db, callback):
        """ Sets the database connection and callback for updates. """
        self.db = db
        self.update_callback = callback

    def show_popup(self, instance):
        """ Displays a popup for storing product name and price. """
        layout = GridLayout(cols=2, spacing=10)

        layout.add_widget(Label(text="Product Name:"))
        self.product_name_input = TextInput(hint_text="Enter product")
        layout.add_widget(self.product_name_input)

        layout.add_widget(Label(text="Product Price:"))
        self.product_price_input = TextInput(hint_text="Enter price", input_filter='float')
        layout.add_widget(self.product_price_input)

        submit_btn = Button(text="Submit", size_hint=(None, None), size=(100, 50))
        submit_btn.bind(on_press=self.store_product)
        layout.add_widget(submit_btn)

        self.popup = Popup(title="Store Product", content=layout, size_hint=(None, None), size=(400, 300))
        self.popup.open()

    def store_product(self, instance):
        """ Stores product details in the database. """
        name = self.product_name_input.text.strip()
        try:
            price = float(self.product_price_input.text.strip())
            if name and price:
                self.db.store_product(name, str(price))
                if self.update_callback:
                    self.update_callback()
            self.popup.dismiss()
        except ValueError:
            self.product_price_input.text = "Invalid!"
