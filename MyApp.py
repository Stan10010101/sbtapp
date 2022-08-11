from kivy.app import App
from kivy.metrics import dp
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from random import choices
from random import randint
from kivy.clock import Clock



class MyApp(App):
    pass


# класс страницы меню
class MenuScreen(Screen):
    pass


# класс страницы заданий
#class Plus_minus_bubb(Bubble):

#    def __init__(self, **kwargs):
#        super().__init__(**kwargs)

    # функция нажатия на кнопки бабла
#    def on_bubb_click(self):
#        print("Bubb clicked")


class TaskScreen(Screen):
    my_text = StringProperty('Ветка')
    my_task = StringProperty('Задания')
    my_time = StringProperty('0')


    # конструктор класса
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = 0
        self.text = None
        self.task = None

    def timer(self, time):
        while True:
            for i in range(self.time):
                yield (i)
            my_time = 0

    def on_start(self):
        self.function_interval = Clock.schedule_interval(self.update_label, 1)
        Clock.schedule_once(self.stop_interval, int(self.ids.time.text)+1)

    def update_label(self, *args):
        self.ids.time.text = str(int(self.ids.time.text) - 1)

    def stop_interval(self, *args):
        self.function_interval.cancel()


    # функция нажатия на кнопку "Начать"
    def on_button_click(self):
        text = ['ветка 1', 'ветка 2', 'ветка 3', 'ветка 4']
        task = ['фкр', 'рт', 'коп1', 'коп2', 'коп5']

        self.time = randint(1, 50) * 10
        n = randint(0, 3)
        m = randint(0, 4)
        self.text = text[n]
        self.task = task[m]

        self.my_text = str(self.text)
        self.my_task = str(self.task)
        self.my_time = str(self.time)



    # создаем бабл
#    def show_bubble(self):
#        self.add_widget(Plus_minus_bubb())


# To DO:

# если выпадает коп5 то автоматически с ним создается число секунд задания,
# форматированное 01:00

# 2 варианта баблов, первый с 2 кнопками (+ и -), второй с 3 кнопками
# (для коп5 кнопки +, - и таймер)

# кнопка таймер(из бабла) должна брать цыфру из последовательности
# в лейбл(коп5) и запускать обратный отсчет, обратный отсчет может
# обновлять или нет длительность коп5 в конце вывести в лейбл "Конец", можно
# удалить текст лейбла а потом вывести "Конец"


if __name__ == '__main__':
    MyApp().run()
