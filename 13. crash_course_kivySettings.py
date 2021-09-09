from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.settings import SettingsWithSidebar

Builder.load_string('''
<Interface>:
    orientation: 'vertical'
    Button:
        text: 'Open the settings'
        font_size: 50 
        on_release: app.open_settings()
''')


class Interface(BoxLayout):
    pass


class SettingsApp(App):
    def build(self):
        self.settings_cls = SettingsWithSidebar
        return Interface()

    # Settings de la app en particular
    def build_config(self, config):
        config.setdefault()


SettingsApp().run()
