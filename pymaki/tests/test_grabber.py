from unittest import TestCase

import grabber

class TestGrabber(TestCase):
    def test_is_string(self):
        s = MakiIcon('bar').get_icon()
        self.assertTrue(isinstance(s, basestring))
