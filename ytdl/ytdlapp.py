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

        with youtube_dl.YoutubeDL(options) as ydl:
            url = 'http://www.youtube.com/watch?v=BaW_jenozKcj'
            dl_thread = threading.Thread(target=ydl.download, args=([url],))
            dl_thread.start()

    def build(self):
        return self.root
