from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.properties import NumericProperty


class Manager(ScreenManager):
    pass
class Menu(Screen):
    pass
class Game(Screen):
    def on_enter(self, *args):
        Clock.schedule_interval(self.update,1/30)

    def update(self,*args):
        self.ids.player.speed += -self.height * 1/30
        self.ids.player.y += self.ids.player.speed * 1/30

    def on_touch_down(self, *args):
        self.ids.player.speed = self.height*0.7
class Player(Image):
    speed = NumericProperty(0)
class HashBird(App):
    pass


HashBird().run()