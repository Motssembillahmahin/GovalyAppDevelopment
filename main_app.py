# File: main_app.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from profile_dashboard import ProfileDashboard
from main_layout import MainLayout


class MainApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='horizontal', **kwargs)

        self.profile_section = ProfileDashboard(size_hint=(0.3, 1))
        self.add_widget(self.profile_section)

        self.main_layout = MainLayout(self.profile_section, size_hint=(0.7, 1))
        self.add_widget(self.main_layout)


class MyApp(App):
    def build(self):
        return MainApp()


if __name__ == '__main__':
    MyApp().run()