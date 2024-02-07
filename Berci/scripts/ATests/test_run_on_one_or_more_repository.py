from unittest import TestCase


class Test(TestCase):
    def test_get_remote_image_tags(self):
        expected = ['0.1.0-SNAPSHOT', ]
        self.assertListEqual()
