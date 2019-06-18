import unittest

from jeraconv import jeraconv


class TestJeraconv(unittest.TestCase):
    """
    test class for jeraconv.py
    """

    @classmethod
    def setUpClass(cls):
        # procedures before tests are started. This code block is executed only once
        pass

    @classmethod
    def tearDownClass(cls):
        # procedures after tests are finished. This code block is executed only once
        pass

    def setUp(self):
        # procedures before every tests are started. This code block is executed every time
        self.jc = jeraconv.J2W()

    def tearDown(self):
        # procedures after every tests are finished. This code block is executed every time
        pass

    def test_jeraconv_basic(self):
        self.assertEqual(645, self.jc.convert('大化元年'))
        self.assertEqual(645, self.jc.convert('大化1年'))
        self.assertEqual(645, self.jc.convert('大化01年'))
        self.assertEqual(645, self.jc.convert('大化１年'))
        self.assertEqual(645, self.jc.convert('大化０１年'))
        self.assertEqual(649, self.jc.convert('大化5年'))
        self.assertEqual(650, self.jc.convert('大化6年'))

        self.assertEqual(2019, self.jc.convert('令和元年'))
        self.assertEqual(2019, self.jc.convert('令和1年'))
        self.assertEqual(2019, self.jc.convert('令和01年'))
        self.assertEqual(2019, self.jc.convert('令和１年'))
        self.assertEqual(2019, self.jc.convert('令和０１年'))
        self.assertEqual(2117, self.jc.convert('令和99年'))
        self.assertEqual(2117, self.jc.convert('令和９９年'))

    def test_jeraconv_errors(self):
        self.assertRaises(ValueError, self.jc.convert, '大化0年')
        self.assertRaises(ValueError, self.jc.convert, '大化00年')
        self.assertRaises(ValueError, self.jc.convert, '大化０年')
        self.assertRaises(ValueError, self.jc.convert, '大化００年')
        self.assertRaises(ValueError, self.jc.convert, '大化7年')
        self.assertRaises(ValueError, self.jc.convert, '大化07年')
        self.assertRaises(ValueError, self.jc.convert, '大化７年')
        self.assertRaises(ValueError, self.jc.convert, '大化０７年')

        self.assertRaises(ValueError, self.jc.convert, '牌孫元年')
        self.assertRaises(ValueError, self.jc.convert, '牌孫1年')
        self.assertRaises(ValueError, self.jc.convert, '牌孫01年')
        self.assertRaises(ValueError, self.jc.convert, '牌孫１年')
        self.assertRaises(ValueError, self.jc.convert, '牌孫０１年')


if __name__ == '__main__':
    unittest.main()
