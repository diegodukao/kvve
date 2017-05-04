from pathlib import Path

from kivymd.list import MDList, TwoLineListItem


class VideosList(MDList):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        path = Path("./videos")
        filepaths = list(path.glob('**/*.*'))

        for fpath in filepaths:
            self.add_widget(
                TwoLineListItem(text=fpath.name[:40] + "..."))
