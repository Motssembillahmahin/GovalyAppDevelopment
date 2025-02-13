from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class MainLayout(BoxLayout):
    def __init__(self, profile_section, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.profile_section = profile_section

        self.total_amount = 0

        # Button Grid Layout
        self.button_grid = GridLayout(cols=2, size_hint=(1, 0.6))

        self.button1 = Button(text='Add to Total', size_hint=(1, 0.2))
        self.button1.bind(on_press=self.add_to_total)
        self.button_grid.add_widget(self.button1)

        self.button2 = Button(text='Store Data', size_hint=(1, 0.2))
        self.button_grid.add_widget(self.button2)

        self.button3 = Button(text='Clear Inputs', size_hint=(1, 0.2))
        self.button_grid.add_widget(self.button3)

        self.button4 = Button(text='Reset Total', size_hint=(1, 0.2))
        self.button_grid.add_widget(self.button4)

        self.button5 = Button(text='Show Data', size_hint=(1, 0.2))
        self.button_grid.add_widget(self.button5)

        self.button6 = Button(text='Exit', size_hint=(1, 0.2))
        self.button_grid.add_widget(self.button6)

        self.add_widget(self.button_grid)

    def add_to_total(self, instance):
        try:
            value = float(instance.text)
            self.total_amount += value
            instance.text = f'Total: {self.total_amount}'
        except ValueError:
            instance.text = 'Invalid Input'