from kivy.app import App
from kivy.uix.button import Button


class FunkyButton(Button):
    pass


class TerceraApp(App):
    def build(self):
        return FunkyButton(
            pos=(100, 100),
            size_hint=(0.5, 0.5)
        )


if __name__ == '__main__':
    TerceraApp().run()
