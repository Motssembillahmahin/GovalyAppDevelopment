from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, RoundedRectangle
from kivy.animation import Animation
from kivy.uix.label import Label
from Button1 import Button1
from Button2 import Button2
from button3 import Button3
from button4 import Button4
from button5 import Button5
from button6 import Button6
from database_manager import DatabaseManager
from profile_dashboard import ProfileDashboard


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='horizontal', **kwargs)
        self.db = DatabaseManager()

        # Background color
        with self.canvas.before:
            Color(0.95, 0.95, 0.95, 1)  # Light gray background
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Left side (Profile Section)
        self.left_side = BoxLayout(orientation='vertical', size_hint=(0.3, 1), padding=20, spacing=20)
        self.profile_section = ProfileDashboard()
        self.left_side.add_widget(self.profile_section)
        self.add_widget(self.left_side)

        # Right side (Main Buttons and Data Display)
        self.right_side = BoxLayout(orientation='vertical', size_hint=(0.7, 1), padding=20, spacing=30)

        # Label for Stored Values
        self.stored_values_label = Label(
            text=self.db.get_stored_products_text(),
            size_hint=(1, 0.1),
            color=(0, 0, 0, 1),
            bold=True
        )
        self.right_side.add_widget(self.stored_values_label)

        # Button Grid Layout
        self.button_grid = GridLayout(cols=2, size_hint=(1, 0.8), spacing=30, padding=20)

        # Button Style (Circular Buttons)
        button_style = {
            'size_hint': (None, None),
            'size': (120, 120),  # Rounded buttons (height=width)
            'background_color': (0.1, 0.6, 0.8, 1),
            'color': (1, 1, 1, 1),
            'bold': True
        }

        # Adding Buttons with Animation
        self.button1 = Button1(**button_style)
        self.button1.set_db_connection(self.db, self.update_stored_values)
        self.add_animation(self.button1)
        self.button_grid.add_widget(self.button1)

        self.button2 = Button2(**button_style)
        self.button2.set_db_connection(self.db, self.update_stored_values)
        self.add_animation(self.button2)
        self.button_grid.add_widget(self.button2)

        self.button3 = Button3(self.db, self.update_stored_values, **button_style)
        self.add_animation(self.button3)
        self.button_grid.add_widget(self.button3)

        self.button4 = Button4(self.db, self.update_stored_values, **button_style)
        self.add_animation(self.button4)
        self.button_grid.add_widget(self.button4)

        self.button5 = Button5(self.db, **button_style)
        self.add_animation(self.button5)
        self.button_grid.add_widget(self.button5)

        self.button6 = Button6(**button_style)
        self.add_animation(self.button6)
        self.button_grid.add_widget(self.button6)

        self.right_side.add_widget(self.button_grid)
        self.add_widget(self.right_side)

    def add_animation(self, button):
        """ Adds an animation effect to the button when clicked. """
        def animate(instance):
            anim = Animation(size=(130, 130), duration=0.1) + Animation(size=(120, 120), duration=0.1)
            anim.start(instance)

        button.bind(on_press=animate)

    def update_stored_values(self):
        """ ✅ Refresh stored products and total sum. """
        self.stored_values_label.text = self.db.get_stored_products_text()
        self.button1.refresh_total()  # ✅ Refresh Button1 text

    def update_rect(self, *args):
        """ Update background rectangle size and position """
        self.rect.size = self.size
        self.rect.pos = self.pos