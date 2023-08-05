from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout


class MainApp(MDApp):
    title = "StellaVideoPlayer"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        player = VideoPlayer(source = input("Enter The Exact Location Of The Video File: "))

        player.state = 'play'

        player.options = {"eos": "loop"}
                
        player.allow_stretch = True

        return player

MainApp().run()

if __name__ == "__main__":
    App.stop
    Window.close()
