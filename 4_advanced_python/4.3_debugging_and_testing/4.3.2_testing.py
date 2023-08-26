# unittest - нужен чтобы протестировать фукциональность, функцию, класс или модуль и посмотреть корректно ли он работает
import unittest


class TestPython(unittest.TestCase):
    def test_float_to_int_coercion(self):
        self.assertEqual(1, int(1.0))

    def test_get_empty_dict(self):
        self.assertIsNone({}.get('key'))

    def test_trueness(self):
        self.assertTrue(bool(10))
