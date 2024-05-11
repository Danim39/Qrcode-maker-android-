import kivy
import segno
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex

class Qrcode(App):
    def build(self):
        self.nm = Label(text='Name or URL', font_size=50, size_hint_y=0.3)
        self.txtname = TextInput(background_color=get_color_from_hex("#9400d3"), size_hint_y=0.5,font_size=50)
        self.txtname.bind(text=self.on_text_change)

    
        
        self.button = Button(text='Generate', font_size=50, size_hint_y=0.5, background_color=get_color_from_hex("#4A148C"))
        self.button.bind(on_press=self.qrcode)
        self.check_button_state()  # Check button state initially
        
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.nm)
        box.add_widget(self.txtname)
        box.add_widget(self.button)
    
        return box

    def on_text_change(self, instance, value):
        self.check_button_state()

    def check_button_state(self):
        if self.txtname.text == "":
            self.button.disabled = True
        else:
            self.button.disabled = False

    def qrcode(self, event):
            
            qrcode = segno.make_qr(self.txtname.text)#Make Qrcode
            qrcode.save(f"Qrcode.png", scale=80)#Save Qrcode
            #---------------------------------------------------

            self.button.text = ""
            self.button.size_hint_y =2
        
            self.nm.text = ""
            self.txtname.background_color = get_color_from_hex("#000000")
            self.txtname.disabled = True
            self.button.background_color = get_color_from_hex("#F8F8F9")
            self.button.background_normal = "Qrcode.png"
            
if __name__=="__main__":
    Qrcode().run()