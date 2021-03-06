from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ColourScreen(Screen):
    colour = ListProperty([1, 0, 0, 1])


class MyScreenManager(ScreenManager):
    pass


root_widget = Builder.load_string('''
MyScreenManager:
    FirstScreen:
    SecondScreen:
<FirstScreen>:
    name: 'first'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'first screen!'
            font_size: 30
        Image:
            source: 'colours.png'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'goto second screen'
                font_size: 30
                # on_release: app.root.current = 'second'
                on_release: print(type(app))
            Button:
                text: 'get random colour screen'
                font_size: 30
<SecondScreen>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'second screen!'
            font_size: 30
        Image:
            source: 'colours2.png'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: 'get random colour screen'
                font_size: 30
<ColourScreen>:
    BoxLayout:
        orientation: 'vertical'
        # colour: random(), random(), random(), 1
        Label:
            text: 'colour {:.2},{:.2},{:.2} screen'.format(*root.colour[:3])
            font_size: 30
        Widget:
            canvas:
                Color:
                    rgba: root.colour
                Ellipse:
                    pos: self.pos
                    size: self.size
        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 30
            Button:
                text: 'get random colour screen'
                font_size: 30
''')

runTouchApp(root_widget)
