import threading

import youtube_dl

from kivy.app import App
from kivymd.theming import ThemeManager


class YtdlApp(App):
    theme_cls = ThemeManager()

    def download(self, url):
        options = {}
        options['ignoreerrors'] = True
        options['outtmpl'] = 'videos/%(title)s-%(id)s.%(ext)s'

        with youtube_dl.YoutubeDL(options) as ydl:
            dl_thread = threading.Thread(target=ydl.download, args=([url],))
            dl_thread.start()

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return self.root
