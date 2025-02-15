from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.graphics import Color, Ellipse
import os

class ProfileDashboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=15, padding=20, **kwargs)

        self.profile_image_path = 'profile_image.png' if os.path.exists('profile_image.png') else 'default_profile.png'

        # Profile Image Container (Ellipse for Circular Effect)
        self.profile_container = BoxLayout(size_hint=(None, None), size=(120, 120))
        with self.profile_container.canvas.before:
            Color(1, 1, 1, 1)  # White border
            self.profile_ellipse = Ellipse(size=self.profile_container.size, pos=self.profile_container.pos)
        self.profile_container.bind(size=self.update_ellipse, pos=self.update_ellipse)

        self.profile_image = Image(source=self.profile_image_path, size_hint=(None, None), size=(120, 120))
        self.profile_container.add_widget(self.profile_image)
        self.add_widget(self.profile_container)

        # Name Input
        self.name_input = TextInput(hint_text="Enter Name", size_hint=(1, 0.2))
        self.add_widget(self.name_input)

        # Upload Button
        self.upload_button = Button(text="Upload Image", size_hint=(1, 0.2), background_color=(0.2, 0.6, 1, 1))
        self.upload_button.bind(on_press=self.open_file_chooser)
        self.add_widget(self.upload_button)

    def open_file_chooser(self, instance):
        """ Opens a file chooser popup to upload an image """
        content = FileChooserIconView()
        popup = Popup(title="Select an Image", content=content, size_hint=(0.9, 0.9))
        content.bind(on_submit=lambda _, selection, __: self.set_image(selection, popup))
        popup.open()

    def set_image(self, selection, popup):
        """ Updates the profile image """
        if selection:
            self.profile_image.source = selection[0]
            self.profile_image_path = selection[0]
            os.system(f'cp "{selection[0]}" profile_image.png')  # Save image persistently
        popup.dismiss()

    def update_ellipse(self, *args):
        """ Ensure ellipse stays circular """
        self.profile_ellipse.size = self.profile_container.size
        self.profile_ellipse.pos = self.profile_container.pos
