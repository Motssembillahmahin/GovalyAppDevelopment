from kivy.uix.button import Button
from kivy.app import App

class Button6(Button):
    def __init__(self, **kwargs):
        super().__init__(text="Exit", **kwargs)
        self.bind(on_press=self.exit_app)

    def exit_app(self, instance):
        """ Exits the application. """
        App.get_running_app().stop()
