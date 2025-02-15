import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner

kivy.require("1.9.1")


class ButtonApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.products = {"Shirt": 0, "Pant": 0, "Shoes": 0}  # Store product prices

    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.btn = Button(text="Open Popup",
                          font_size="20sp",
                          background_color=(0.2, 0.6, 1, 1),
                          size_hint=(None, None),
                          size=(200, 100),
                          pos=(300, 250))
        self.btn.bind(on_press=self.show_popup)

        self.total_label = Label(text="Total Stored Values:\n" + self.get_total_values(), font_size="18sp")

        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.total_label)

        return self.layout

    def show_popup(self, instance):
        popup_layout = GridLayout(cols=2, padding=10, spacing=10)

        popup_layout.add_widget(Label(text="Select Product:"))
        self.product_spinner = Spinner(text="Select", values=list(self.products.keys()) + ["+ Add New"])
        self.product_spinner.bind(text=self.check_add_new_product)
        popup_layout.add_widget(self.product_spinner)

        popup_layout.add_widget(Label(text="Enter Amount:"))
        self.amount_input = TextInput(hint_text="Enter amount", multiline=False, input_filter='int')
        popup_layout.add_widget(self.amount_input)

        submit_btn = Button(text="Submit", size_hint=(None, None), size=(100, 50))
        submit_btn.bind(on_press=self.update_values)

        popup_layout.add_widget(submit_btn)

        self.popup = Popup(title="Enter Product Prices",
                           content=popup_layout,
                           size_hint=(None, None), size=(400, 300))
        self.popup.open()

    def check_add_new_product(self, spinner, text):
        if text == "+ Add New":
            self.show_add_product_popup()

    def show_add_product_popup(self):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_layout.add_widget(Label(text="Enter New Product Name:"))
        self.new_product_input = TextInput(hint_text="Product name", multiline=False)
        popup_layout.add_widget(self.new_product_input)

        submit_btn = Button(text="Add Product")
        submit_btn.bind(on_press=self.add_new_product)
        popup_layout.add_widget(submit_btn)

        self.add_product_popup = Popup(title="Add New Product",
                                       content=popup_layout,
                                       size_hint=(None, None), size=(300, 200))
        self.add_product_popup.open()

    def add_new_product(self, instance):
        new_product = self.new_product_input.text.strip()
        if new_product and new_product not in self.products:
            self.products[new_product] = 0
            self.product_spinner.values = list(self.products.keys()) + ["+ Add New"]
            self.product_spinner.text = new_product
        self.add_product_popup.dismiss()

    def update_values(self, instance):
        selected_product = self.product_spinner.text
        if selected_product in self.products:
            try:
                value = int(self.amount_input.text)
                self.products[selected_product] += value
                self.total_label.text = "Total Stored Values:\n" + self.get_total_values()
            except ValueError:
                pass  # Ignore invalid inputs
        self.popup.dismiss()

    def get_total_values(self):
        return "\n".join([f"{product}: {price}" for product, price in self.products.items()])


if __name__ == "__main__":
    ButtonApp().run()
