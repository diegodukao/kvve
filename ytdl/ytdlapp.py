import threading

import youtube_dl

from kivy.app import App


class YtdlApp(App):
    """Basic kivy app

    Edit ytdl.kv to get started.
    """
    def download(self, url):
        options = {}
        options['ignoreerrors'] = True
        options['outtmpl'] = 'videos/%(title)s-%(id)s.%(ext)s'

        with youtube_dl.YoutubeDL(options) as ydl:
            dl_thread = threading.Thread(target=ydl.download, args=([url],))
            dl_thread.start()

    def build(self):
        return self.root
