import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        self.screen = GridLayout(cols=2)
        self.screen.add_widget(Label(text='Enter smoke temperature'))
        self.temp = TextInput()
        self.screen.add_widget(self.temp)
        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.confirm)
        self.screen.add_widget(self.submit)
        self.output = Label()
        self.screen.add_widget(self.output)
        return self.screen

    def confirm(self, instance):
        print(int(self.temp.text))
        smoketemp = 0
        smoketemp = int(self.temp.text)
        adjustedtemp = smoketemp * 1.28
        if int(adjustedtemp) <= 355:
            self.output.text = "1 pod needs to be deployed."
        elif int(adjustedtemp) > 355 and int(adjustedtemp) <= 375:
            self.output.text = "2 pods need to be deployed."
        elif int(adjustedtemp) > 375:
            self.output.text = "3 pods needs to be deployed."
    
    


MainApp().run()
