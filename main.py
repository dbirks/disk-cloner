import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from subprocess import call

class InitialScreen(GridLayout):
    
    def __init__(self, **kwargs):
        super(InitialScreen, self).__init__(**kwargs)

        def callback1(instance):
            cmd = 'sudo hdparm -I /dev/sda | grep "Model" | sed "s/[[:space:]]Model Number:[[:space:]]\+//g"'
            call(str(cmd), shell=True)
            
        self.cols = 2
        btn1 = Button(text='List disks')
        btn1.bind(on_press=callback1)
        self.add_widget(btn1)
        self.add_widget(Button(text='About'))

class MyApp(App):

    def build(self):
        return InitialScreen()

if __name__ == '__main__':
    MyApp().run()
