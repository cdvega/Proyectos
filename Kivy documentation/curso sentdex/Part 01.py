import kivy
from kivy.uix.label import Label
from kivy.app import App
kivy.require('2.0.0')


class SimpleKivy(App):
    def build(self):
        return Label(text='Hello world!')


if __name__ == '__main__':
    SimpleKivy().run()
