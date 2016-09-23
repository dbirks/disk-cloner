import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.button import Label
from subprocess import *

class InitialScreen(GridLayout):
    
    def __init__(self, **kwargs):
        super(InitialScreen, self).__init__(**kwargs) # who knows

        disk_models = ['oh','hai']

        # Get a list of available disks
        cmd = 'lsblk -ln | grep -o "\<[[:alpha:]][[:alpha:]][[:alpha:]][^[:digit:]]*\>" | grep sd'
        disk_names = check_output(cmd, shell=True) # pull in list of disks
        disk_names = disk_names.decode().split('\n') # remove newlines, make list
        disk_names.pop() # remove last list item (an empty newline)

        # Get disk model info
        for i, disk in enumerate(disk_names):
            cmd = 'sudo hdparm -I /dev/%s | grep "Model" | sed "s/[[:space:]]Model Number:[[:space:]]\+//g"' % disk
            out = (check_output(cmd, shell=True)).decode()
            out = out.rstrip(' \n')             
            disk_models[i] = out

        self.cols = 3
        self.rows = 2
        self.spacing = [5,40]
        input_disk = 'bleh'
        output_disk = 'meh'

        # column 1
        self.add_widget(Label(text='Input disk:'))
        # button 1
        def set_input(instance):
            global input_disk 
            input_disk = disk_names[0]
        btn1 = Button(text=disk_names[0] + '\n' + disk_models[0])
        self.add_widget(btn1)
        btn1.bind(on_press = set_input)
        # button 2
        def set_input(instance):
            global input_disk 
            input_disk = disk_names[1]
        btn2= Button(text=disk_names[1] + '\n' + disk_models[1])
        self.add_widget(btn2)
        btn2.bind(on_press = set_input)

        # column 2
        self.add_widget(Label(text='Output disk:'))
        # button 3
        def set_output(instance):
            global output_disk 
            output_disk = disk_names[0]
        btn3 = Button(text=disk_names[0] + '\n' + disk_models[0])
        self.add_widget(btn3)
        btn3.bind(on_press = set_output)
        # button 4
        def set_output(instance):
            global output_disk 
            output_disk = disk_names[1]
        btn4= Button(text=disk_names[1] + '\n' + disk_models[1])
        self.add_widget(btn4)
        btn4.bind(on_press = set_output)

        print('in:' + input_disk)
        print('out:' + output_disk)


class MyApp(App):

    def build(self):
        return InitialScreen()

if __name__ == '__main__':
    MyApp().run()
