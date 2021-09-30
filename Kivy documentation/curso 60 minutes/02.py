from kivy.app import App
from kivy.uix.button import Button


class FunkyButton(Button):
    def __init__(self, **kwargs):
        super(FunkyButton, self).__init__(**kwargs)
        self.text = 'Funky button'
        self.pos = (100, 100)
        self.size_hint = (0.25, 0.25)


class PrimeraApp(App):
    def build(self):
        return FunkyButton()


if __name__ == '__main__':
    PrimeraApp().run()
