from Darkorbit.authorization import DarkorbitAuth


def run():
    test = DarkorbitAuth()
    test.authorize()
    print(test.info)
    print(test.skylab)
    print(test.skylab_lvls)
