# Imports
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.fitimage import FitImage
from kivymd.uix.button import MDFloatingActionButton
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty

main_data = {'0_0': """Добро пожаловать в Сагу битв и Приключений
                      вы готовы начать?""",
             '1_0': """Поехали. Вы бомж.""",
             '1_1': """Досвидания!!!"""}


class MenuScreen(Screen):
    pass


class GameScreen(Screen):
    label_wig = ObjectProperty(defaultvalue=main_data['0_0'])
    save_number = StringProperty(defaultvalue='0_0')
    variant = StringProperty(defaultvalue='0')

    def next_step(self, save_number, variant):
        #print(main_data[str(eval(save_number[4:]+'+1'))])
        if variant == '0':
            save_number = str(eval(save_number.strip('_')[0]+'+1'))+'_'+variant
            print('Current_step: '+save_number)
        else:
            save_number = str(eval(save_number.strip('_')[0] + '+1')) + '_' + variant
            print('Current_step: '+save_number)
        self.label_wig = main_data[save_number] + f"{save_number}"

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
