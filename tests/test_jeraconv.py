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
        self.j2w = jeraconv.J2W()
        self.w2j = jeraconv.W2J()

    def tearDown(self):
        # procedures after every tests are finished. This code block is executed every time
        pass

    def test_jeraconv_j2w_basic(self):
        self.assertEqual(645, self.j2w.convert('大化元年'))
        self.assertEqual(645, self.j2w.convert('大化1年'))
        self.assertEqual(645, self.j2w.convert('大化01年'))
        self.assertEqual(645, self.j2w.convert('大化１年'))
        self.assertEqual(645, self.j2w.convert('大化０１年'))
        self.assertEqual(649, self.j2w.convert('大化5年'))
        self.assertEqual(650, self.j2w.convert('大化6年'))

        self.assertEqual(2019, self.j2w.convert('令和元年'))
        self.assertEqual(2019, self.j2w.convert('令和1年'))
        self.assertEqual(2019, self.j2w.convert('令和01年'))
        self.assertEqual(2019, self.j2w.convert('令和１年'))
        self.assertEqual(2019, self.j2w.convert('令和０１年'))
        self.assertEqual(2117, self.j2w.convert('令和99年'))
        self.assertEqual(2117, self.j2w.convert('令和９９年'))

        self.assertEqual(2020, self.j2w.convert('平成32年', limit_check=False))

    def test_jeraconv_j2w_errors(self):
        self.assertRaises(ValueError, self.j2w.convert, '大化0年')
        self.assertRaises(ValueError, self.j2w.convert, '大化00年')
        self.assertRaises(ValueError, self.j2w.convert, '大化０年')
        self.assertRaises(ValueError, self.j2w.convert, '大化００年')
        self.assertRaises(ValueError, self.j2w.convert, '大化7年')
        self.assertRaises(ValueError, self.j2w.convert, '大化07年')
        self.assertRaises(ValueError, self.j2w.convert, '大化７年')
        self.assertRaises(ValueError, self.j2w.convert, '大化０７年')

        self.assertRaises(ValueError, self.j2w.convert, '牌孫元年')
        self.assertRaises(ValueError, self.j2w.convert, '牌孫1年')
        self.assertRaises(ValueError, self.j2w.convert, '牌孫01年')
        self.assertRaises(ValueError, self.j2w.convert, '牌孫１年')
        self.assertRaises(ValueError, self.j2w.convert, '牌孫０１年')

        self.assertRaises(ValueError, self.j2w.convert, '平成32年', limit_check=True)

    def test_jeraconv_w2j_basic(self):
        self.assertEqual('令和1年5月1日', self.w2j.convert(2019, 5, 1))
        self.assertEqual('令和1年5月1日', self.w2j.convert(2019, 5, 1, return_type='str'))
        self.assertEqual({'era': '令和', 'year': 1, 'month': 5, 'day': 1},
                         self.w2j.convert(2019, 5, 1, return_type='dict'))
        self.assertEqual(['令和', 1, 5, 1], self.w2j.convert(2019, 5, 1, return_type='list'))
        self.assertEqual(('令和', 1, 5, 1), self.w2j.convert(2019, 5, 1, return_type='tuple'))

    def test_jeraconv_w2j_errors(self):
        self.assertRaises(ValueError, self.w2j.convert, 2019, 5, 1, return_type='other')


if __name__ == '__main__':
    unittest.main()
