from kivy.app import App
from kivy.uix.button import Button


class PrimeraApp(App):
    def build(self):
        return Button(
            text='Hola mundo',
            pos=(50, 50),
            size=(200, 100),
            # necesario para que funcione size en términos absolutos:
            size_hint=(None, None)
        )


if __name__ == '__main__':
    PrimeraApp().run()
