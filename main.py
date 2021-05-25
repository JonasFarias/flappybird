from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

class HashBird(App):
    def build(self):
        player = Image(source='attack_1.png')
        layout = FloatLayout()
        layout.add_widget(player)
        return layout


HashBird().run()