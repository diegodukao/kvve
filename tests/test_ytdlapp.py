#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from kvve.kvveapp import KvveApp


class TestKvveApp(unittest.TestCase):
    """TestCase for KvveApp.
    """
    def setUp(self):
        self.app = KvveApp()

    def test_name(self):
        self.assertEqual(self.app.name, 'kvve')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
