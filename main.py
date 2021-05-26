from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

class Manager(ScreenManager):
    pass
class Menu(Screen):
    pass
class Game(Screen):
    pass
class Player(Image):
    pass
class HashBird(App):
    pass


HashBird().run()