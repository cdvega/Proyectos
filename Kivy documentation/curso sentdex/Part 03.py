from kivy.uix.label import Label
from kivy.app import App


class SimpleKivy(App):
    def build(self):
        return Label()


if __name__ == '__main__':
    SimpleKivy().run()
