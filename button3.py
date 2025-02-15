from kivy.uix.button import Button

class Button3(Button):
    def __init__(self, db, update_callback, **kwargs):
        super().__init__(text="Clear Products", **kwargs)
        self.db = db
        self.update_callback = update_callback
        self.bind(on_press=self.clear_products)

    def clear_products(self, instance):
        """ Clears all stored products. """
        if self.db:
            self.db.clear_products()  # ✅ Now correctly calls clear_products()
            self.update_callback()
        else:
            print("❌ ERROR: Database connection is missing in Button3!")
