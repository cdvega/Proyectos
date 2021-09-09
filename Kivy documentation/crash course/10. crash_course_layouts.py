from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.base import runTouchApp
from kivy.lang import Builder


Builder.load_string('''
<RootWidget>:
    text: 'THE BACKGROUND'
    font_size: 150
    Image:
        # pos: root.pos
        # size: root.width*0.5, root.height
        source: 'colours.png'
        allow_stretch: True
        keep_ratio: False
    Image:
        # pos: root.x + root.width*0.5, root.y
        # size: root.width*0.5, root.height
        source: 'colours2.png'
        allow_stretch: True
        keep_ratio: False
    Image:
        source: 'colours.png'
        allow_stretch: True
        keep_ratio: False
''')


class RootWidget(Label):
    def do_layout(self, *args):
        number_of_children = len(self.children)
        width = self.width
        width_per_child = width // number_of_children
        positions = range(0, width, width_per_child)
        for position, child in zip(positions, self.children):
            child.height = self.height
            child.width = width_per_child
            child.y = self.y
            child.x = self.x + position

    def on_size(self, *args):
        self.do_layout()

    def on_pos(self, *args):
        self.do_layout(*args)

    def add_widget(self, widget):
        super(RootWidget, self).add_widget(widget)
        self.do_layout()

    def remove_widget(self, widget):
        super(RootWidget, self).remove_widget(widget)
        self.do_layout()


runTouchApp(RootWidget())
