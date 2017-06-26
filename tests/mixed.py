import unittest

from mixed import Mixed


class TestMixedNumbers(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(Mixed(0), Mixed(0.0))
        self.assertEqual(Mixed(0), Mixed(''))
        self.assertEqual(Mixed(0), Mixed(False))
        self.assertFalse(Mixed(0))
        print('OK zero check')

    def test_positive(self):
        self.assertEqual(Mixed(.54), .54)
        self.assertEqual(Mixed(1), 1)
        self.assertEqual(Mixed(3.333333), 3.333333)
        self.assertTrue(Mixed(.0001))
        self.assertTrue(Mixed(.2))
        self.assertTrue(Mixed(1234.5))
        print('OK positive numbers check')

    def test_negative(self):
        # TODO: test negative mixed numbers work properly
        pass


if __name__ == '__main__':
    unittest.main()
