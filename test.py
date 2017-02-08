import unittest
from text import generate_buttons


class TestClass(unittest.TestCase):
    def test_button_generator(self):
        s = '<div id="button-box"><button onclick="getAjaxData(1)" class="mui-btn mui-btn--raised mui-btn--primary">1</button></div>'
        self.assertEqual(generate_buttons({'1': 1}), s)


if __name__ == '__main__':
    unittest.main()
