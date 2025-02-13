from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
import os


class ProfileDashboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.profile_image_path = 'default_profile.png'
        if os.path.exists('profile_image.png'):
            self.profile_image_path = 'profile_image.png'

        self.profile_image = Image(source=self.profile_image_path, size_hint=(None, None), size=(100, 100))
        self.add_widget(self.profile_image)

        self.name_input = TextInput(hint_text='Enter Name', size_hint=(1, 0.2))
        self.add_widget(self.name_input)

        self.upload_button = Button(text='Upload Image', size_hint=(1, 0.2))
        self.upload_button.bind(on_press=self.open_file_chooser)
        self.add_widget(self.upload_button)

    def open_file_chooser(self, instance):
        content = FileChooserIconView()
        popup = Popup(title='Select an Image', content=content, size_hint=(0.9, 0.9))
        content.bind(on_submit=lambda _, selection, __: self.set_image(selection, popup))
        popup.open()

    def set_image(self, selection, popup):
        if selection:
            self.profile_image.source = selection[0]
            self.profile_image_path = selection[0]
            os.system(f'cp "{selection[0]}" profile_image.png')  # Save image persistently
        popup.dismiss()
