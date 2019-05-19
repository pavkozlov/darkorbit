import unittest
from Darkorbit.authorization import DarkorbitAuth
import config


class AuthTest(unittest.TestCase):
    def setUp(self):
        self.auth_class = DarkorbitAuth()

    def test_nonauth_class(self):
        '''ПРОВЕРКА НЕАВТОРИЗОВАННОГО КЛАССА'''

        '''ВСЕ ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ = NONE'''
        self.assertEqual(self.auth_class.server, self.auth_class.info, self.auth_class.skylab)
        self.assertEqual(self.auth_class.skylab_lvls, self.auth_class.do_url, None)
        self.assertEqual(self.auth_class.server, self.auth_class.skylab)

        '''SECURITY_TOKEN ИМЕЕТ СТРОКОВЫЙ ТИП И ЕГО ДЛИНА БОЛЬШЕ 0'''
        self.assertEqual(type(self.auth_class.security_token), str)
        self.assertTrue(len(self.auth_class.security_token) != 0)

    def test_authorize(self):
        '''ПРОВЕРКА КЛАССА ПОСЛЕ АВТОРИЗАЦИИ'''

        '''ПОСЛЕ АВТОРИЗАЦИИ ВСЕ ЗНАЧЕНИЯ ЗАПОЛНЕНЫ (НЕ NONE)'''
        self.auth_class.authorize()
        all_items = [self.auth_class.server, self.auth_class.info, self.auth_class.skylab,
                     self.auth_class.skylab_lvls, self.auth_class.do_url]
        self.assertEqual(all(all_items), True)

        '''ПРОЕРЯЕМ ТИПЫ ЗНАЧЕНИЙ И ИХ ДЛИНУ'''
        self.assertEqual(type(self.auth_class.server), str)
        self.assertEqual(len(self.auth_class.info), 6)
        self.assertEqual(type(self.auth_class.info), dict)
        self.assertEqual(len(self.auth_class.skylab), 8)
        self.assertEqual(type(self.auth_class.skylab), dict)
        self.assertEqual(len(self.auth_class.skylab_lvls), 11)
        self.assertEqual(type(self.auth_class.skylab_lvls), dict)

        '''ПРОВЕРЯЕМ ЧТО ВСЕ ЗНАЧЕНИЯ СЛОВАРЕЙ - ЧИСЛОВОГО ТИПА'''
        list1 = list(i for i in self.auth_class.info.values())
        list2 = list(i for i in self.auth_class.skylab.values())
        list3 = list(i for i in self.auth_class.skylab_lvls.values())
        res = list1 + list2 + list3
        result = [s for s in res if type(s) == int]
        self.assertEqual(res, result)

    def test_config(self):
        '''ПРОВЕРКА ФУНКЦИЙ В CONFIG'''

        '''ПРОВЕРКА ФУНКЦИИ RETURN_URL'''
        reality = config.return_url('test777')
        waiting = 'https://test777.darkorbit.com/indexInternal.es?action='
        self.assertEqual(reality, waiting)

        '''ПРОВЕРКА ФУНКЦИИ CLEAN_DATA'''
        input_data = '1,2', 100500, '11.5', '999'
        res = [config.clean_data(i) for i in input_data]
        result = [s for s in res if type(s) == int]
        self.assertEqual(res, result)

    def tearDown(self):
        self.auth_class.session.close()
