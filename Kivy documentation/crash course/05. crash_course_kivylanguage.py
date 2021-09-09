from kivy.app import App

from kivy.uix.boxlayout import BoxLayout


class ScatterTextWidget(BoxLayout):
    pass


class Tutorial2App(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == '__main__':
    Tutorial2App().run()
