from pathlib import Path

from kivy.app import App
from kivy.properties import StringProperty
from kivymd.list import MDList, TwoLineListItem


class VideosListItem(TwoLineListItem):
    path = StringProperty()

    def on_press(self):
        app = App.get_running_app()
        app.root.player.source = self.path


class VideosList(MDList):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        path = Path("./videos")
        filepaths = list(path.glob('**/*.*'))

        for fpath in filepaths:
            self.add_widget(
                VideosListItem(
                    text=fpath.name[:40] + "...",
                    path=str(fpath))
            )
