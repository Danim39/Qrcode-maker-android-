import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Mom(App):
    def build(self):
        lbl=Label(text='Id:')
        txtid=TextInput(multiline=False)

        lbl2=Label(text='Password')
        txtpassword=TextInput(multiline=False)

        button=Button(text='Enter',font_size=50)


        box=BoxLayout(orientation='vertical')
        box.add_widget(lbl)
        box.add_widget(txtid)
        box.add_widget(lbl2)
        box.add_widget(txtpassword)
        box.add_widget(button)


        return box

if __name__=="__main__":
    Mom().run()
