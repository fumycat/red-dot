import unittest
from main import hello_world


class TestClass(unittest.TestCase):
    def test_hello_word(self):
        self.assertEqual(hello_world(), 'Hello World!')


if __name__ == '__main__':
    unittest.main()
