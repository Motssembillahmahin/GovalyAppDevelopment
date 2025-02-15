from kivy.app import App
from main_layout import MainLayout

class MyApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    MyApp().run()
