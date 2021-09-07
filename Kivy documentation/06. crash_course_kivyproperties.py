from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
import random


class ScatterTextWidget(BoxLayout):
    text_colour = ListProperty([1, 0, 0, 1])

    def change_label_colour(self, *args):

        colour = [random.random() for _ in range(3)] + [1]
        self.text_colour = colour


class Tutorial3App(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == '__main__':
    Tutorial3App().run()
