import unittest
import gns3converter


class TestVersion(unittest.TestCase):
    def test_version(self):
        self.assertEqual('1.3.0', gns3converter.__version__)

if __name__ == '__main__':
    unittest.main()
