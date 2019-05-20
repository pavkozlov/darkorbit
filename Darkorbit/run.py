from Darkorbit.authorization import DarkorbitAuth
from Darkorbit.skylab import SkyLab


def run():
    test = DarkorbitAuth()
    test.authorize()

    skylab_test = SkyLab(test)
    skylab_test.update()
