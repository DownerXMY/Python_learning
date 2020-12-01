import unittest
from CH12.unit_test.unit_test import add

class test_add(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
    def test_add_2(self):
        self.assertEqual(add(10, 20), 30)
    def test_add_3(self):
        self.assertNotEqual(add(3, 5), 9)
    def test_add_4(self):
        self.assertRaises(ValueError, add, 1, 'str')

if __name__ == '__main__':
    unittest.main()



