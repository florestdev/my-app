# ОСНОВНОЙ ФАЙЛ КОДА ДЛЯ ПРИЛОЖЕНИЯ ОТ FLOREST DEVELOPER!
# 21.03.2023, права защищены (c).
# Импорты.
import kivy
from kivy import *
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import random
from random import *
import math
from kivy.uix import *
from kivy.extras.highlight import KivyLexer
from kivy.uix.codeinput import CodeInput
from pygments.lexers import *
from kivy.extras import *
from kivy.config import *
from database import *
# Основной код.
user = input('Как вас зовут: ')
class FlorestApp(App):
    def build(self):
        button = Button(text=f'Нажми на кнопочку, {user}. Она исполняет действия.', font_size=20, on_press=self.florest_knopka_press, background_color=[1, 0, 0, 1], background_normal = '')
        return button
    def florest_knopka_press(self, instance):
        print(f'~ ~ ~ ~ ~ ~  Корпорация "Florest Develop.", 21.03.2023 (c). ~ ~ ~ ~ ~ ~')
        print(f'[Лог приложения     ]: Внимание. Кнопка была нажата. Запускаю, процесс..')
        print(f'[Лог приложения     ]: Процесс, по изменению кнопки, успешно запущен.')
        print(f'[Лог приложения     ]: Кнопка была успешно изменена!')
        print(f'[Финансы приложения     ]: Ваш баланс: {balance}')
        instance.text = f'Я изменилась. :).\nFlorest Develop, Inc.'

    
if __name__ == '__main__':
    app = FlorestApp()
    app.run()
