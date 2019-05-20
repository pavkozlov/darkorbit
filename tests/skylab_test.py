import unittest
from Darkorbit.skylab import SkyLab
from Darkorbit.authorization import DarkorbitAuth


class SkyLabTest(unittest.TestCase):
    def setUp(self):
        auth = DarkorbitAuth()
        auth.authorize()
        self.skylab_test = SkyLab(auth)

    def test_upd_skylab(self):
        r = self.skylab_test.upd_skylab()
        self.assertEqual(type(r), list)

    def tearDown(self):
        self.skylab_test.session.close()
