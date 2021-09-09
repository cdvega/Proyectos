from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

# porque esto va a ser un simple widget, no una app completa
from kivy.base import runTouchApp
from kivy.lang import Builder  # para escribir aquí en kivy language


Builder.load_string('''
<ScrollableLabel>:
    text: ('Un texto muy muy largo ')*100
    Label:
        text: root.text
        font_size: 50
        text_size: self.width, None
        size_hint_y: None
        # La altura del Label es la del texto; eso fuerza la necesidad de scrolling
        height: self.texture_size[1]  
''')


class ScrollableLabel(ScrollView):
    pass


runTouchApp(ScrollableLabel())
