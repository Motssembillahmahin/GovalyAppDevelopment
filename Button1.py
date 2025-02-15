from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class Button1(Button):
    def __init__(self, **kwargs):
        super().__init__(text="Total: 0", **kwargs)
        self.db = None  # Ensure it's set later
        self.update_callback = None
        self.bind(on_press=self.show_popup)

    def set_db_connection(self, db, callback):
        """ Sets the database connection and callback for updates. """
        self.db = db
        self.update_callback = callback
        self.refresh_total()

    def show_popup(self, instance):
        """ Displays a popup to enter a number for addition. """
        layout = GridLayout(cols=1, spacing=10)

        self.input_field = TextInput(hint_text="Enter a number", multiline=False)
        submit_btn = Button(text="Submit", size_hint=(None, None), size=(100, 50))
        submit_btn.bind(on_press=self.add_to_total)

        layout.add_widget(Label(text="Enter a number to add:"))
        layout.add_widget(self.input_field)
        layout.add_widget(submit_btn)

        self.popup = Popup(title="Enter Value", content=layout, size_hint=(None, None), size=(300, 200))
        self.popup.open()

    def add_to_total(self, instance):
        """ Adds input value to total sum in database. """
        if self.db is None:
            print("❌ ERROR: Database connection is missing in Button1!")
            return  # Prevents crash if db is None

        try:
            value = int(self.input_field.text.strip())
            latest_sum = self.db.get_latest_sum()
            new_sum = latest_sum + value
            self.db.update_sum(new_sum)
            self.refresh_total()
            if self.update_callback:
                self.update_callback()
            self.popup.dismiss()
        except ValueError:
            self.input_field.text = "Invalid!"

    def refresh_total(self):
        """ Refreshes the button text to show the updated sum. """
        if self.db:
            self.text = f"Total: {self.db.get_latest_sum()}"
