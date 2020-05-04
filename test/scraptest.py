from scrapper import scrapper
import unittest


class ScrapperTestCase(unittest.TestCase):
    test_values = ("rai3863349342466", 22.00)

    def test_scrapper(self):
        for value, expected in self.test_values:
            self.assertEqual(expected, scrapper.parse_price(value))


if __name__ == '__main__':
    unittest.main()
