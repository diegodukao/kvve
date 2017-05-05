=============================
kvve
=============================

Video player in Kivy that download videos from Youtube (and a lot of others).


Requirements
------------
- Kivy 1.92 (dev)
- KivyMD
- youtube-dl

Obs
---
There's a wicked workaround needed in youtube-dl to make it work with kvve.
You need to go to `utils.py` in youtube_dl instalation and comment/remove (yes, it's
that bad) from line 1398 to 1401 (sorry).
This is the code that needs to be removed::

    elif hasattr(out, 'buffer'):
        enc = encoding or getattr(out, 'encoding', None) or preferredencoding()
        byt = s.encode(enc, 'ignore')
        out.buffer.write(byt)```

Features
--------

- Download videos
- Play videos


Launching the app
~~~~~~~~~~~~~~~~~

`Kivy`_ is compatible with Python 2 as well as Python 3::

    cd kvve
    python main.py

