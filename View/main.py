# Imports
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class MenuScreen(Screen):
    print('1111')


class ProfileScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))


class TextQuest(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        screen = Builder.load_file('main.kv')
        return screen


if __name__ == '__main__':
    TextQuest().run()
