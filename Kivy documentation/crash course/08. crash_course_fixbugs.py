from os import close
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.graphics.context_instructions import Color
import random


class ScatterTextWidget(BoxLayout):
    text_colour = ListProperty([1, 0, 0, 1])

    def __init__(self, **kwargs):
        super(ScatterTextWidget, self).__init__(**kwargs)

    def change_label_colour(self, *args):

        colour = [random.random() for _ in range(3)] + [1]
        self.text_colour = colour


class Tutorial08App(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == '__main__':
    Tutorial08App().run()
