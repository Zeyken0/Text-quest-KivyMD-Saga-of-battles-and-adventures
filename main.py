# Imports
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.fitimage import FitImage
from kivymd.uix.button import MDFloatingActionButton
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty

user_data = {''}
save_data = {'0_1': {'accept': '1_0', 'reject': '1_1'},
             '1_0': {'accept': '2_0', 'reject': '2_1'},
             '1_1': {'accept': '2_0', 'reject': '2_1'}}
text_data = {'0_0': """Добро пожаловать в Сагу битв и Приключений
                      вы готовы начать?""",
             '0_1': """БЛА БЛА БЛА""",
             '1_0': """Поехали. Вы бомж.""",
             '1_1': """Досвидания!!!""",
             '2_0': """ff""",
             '2_1': """fffff"""}


class MenuScreen(Screen):
    pass


class GameScreen(Screen):
    label_wig = ObjectProperty(defaultvalue=text_data['0_0'])
    save_number = StringProperty(defaultvalue='0_1')
    variant = StringProperty(defaultvalue='0')

    def next_step(self, save_number: str, variant: str):
        if variant == '0':
            self.save_number = save_data[save_number]['accept']
            print('Current_step: ' + save_number)
            self.label_wig = text_data[save_number]
        else:
            self.save_number = save_data[save_number]['reject']
            print('Current_step: ' + save_number)
            self.label_wig = text_data[save_number]


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
