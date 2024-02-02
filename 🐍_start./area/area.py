import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require('2.0.0')
class Areaapp(App):
    def build(self):
        #background
        #self.window.add_widget(Image(source="8084.jpg"))
        #title
        
        self.Heading = Label(text="Area of a Circle")
        self.window.add_widget(self.Heading)
        return self.window
    
        
if __name__ == "__main__":
    Areaapp().run()