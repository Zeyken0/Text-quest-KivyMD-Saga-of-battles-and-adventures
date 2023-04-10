# Imports
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.fitimage import FitImage
from kivymd.uix.button import MDFloatingActionButton
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class MenuScreen(Screen):
    pass


class GameScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(GameScreen(name='game'))


class TextQuest(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        screen = Builder.load_file('View/main.kv')
        return screen
#white-background

if __name__ == '__main__':
    TextQuest().run()
