# Imports
import json
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.fitimage import FitImage
from kivymd.uix.button import MDFloatingActionButton
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty

with open('data.json', "r", encoding='utf-8') as r:
    main_data = json.loads(r.read())
for i in main_data['save_data']:
    print(i)


class MenuScreen(Screen):
    pass


class GameScreen(Screen):
    label_wig = ObjectProperty(defaultvalue=main_data['save_data']['0_0']['save_text'])
    save_number = StringProperty(defaultvalue='0_1')
    variant = StringProperty(defaultvalue='0')

    def next_step(self, save_number: str, variant: str):
        if variant == '0':
            self.save_number = main_data['save_data'][save_number]['accept']
            print('Current_step: ' + save_number)
            self.label_wig = main_data['save_data'][save_number]['save_text']
        else:
            self.save_number = main_data['save_data'][save_number]['reject']
            print('Current_step: ' + save_number)
            self.label_wig = main_data['save_data'][save_number]['save_text']


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(GameScreen(name='game'))


class TextQuest(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        screen = Builder.load_file('View/main.kv')
        return screen


# white-background

if __name__ == '__main__':
    TextQuest().run()
    r.close()
