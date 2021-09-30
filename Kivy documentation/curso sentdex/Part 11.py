## Drawing app ##

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line


class Painter(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MainScreen(Screen):
    pass


class AnotherScreen(Screen):
    pass


class MainApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AnotherScreen(name='other',))
        return sm


if __name__ == '__main__':
    MainApp().run()
