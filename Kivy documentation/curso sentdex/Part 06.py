## Float Layout ##

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class SimpleKivy4(App):
    def build(self):
        return FloatLayout()


if __name__ == '__main__':
    SimpleKivy4().run()
