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

        #def choose_disk(instance):
        #    cmd = 'sudo hdparm -I /dev/sda | grep "Model" | sed "s/[[:space:]]Model Number:[[:space:]]\+//g"'
        #    call(str(cmd), shell=True)
            
        self.cols = 2

        def set_input(disk):
            input_disk = disk_names[disk]
            print(input_disk)

        # column 1
        self.add_widget(Label(text='Input disk:'))
        for i, disk in enumerate(disk_names):
            btn = Button(text=disk_names[i] + '\n' + disk_models[i])
            self.add_widget(btn)
            btn.bind(on_press = set_input(str(i))) ######
        
        
        # column 2
        self.add_widget(Label(text='Output disk:'))
        btnOutput1 = Button(text='sda')
        self.add_widget(btnOutput1)
        self.add_widget(Button(text='sdb'))

class MyApp(App):

    def build(self):
        return InitialScreen()

if __name__ == '__main__':
    MyApp().run()
