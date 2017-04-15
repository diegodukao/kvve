#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from ytdl.ytdlapp import YtdlApp


class TestYtdlApp(unittest.TestCase):
    """TestCase for YtdlApp.
    """
    def setUp(self):
        self.app = YtdlApp()

    def test_name(self):
        self.assertEqual(self.app.name, 'ytdl')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
