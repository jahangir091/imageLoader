import os
import unittest

from main import saveImages
from main import PROJECT_ROOT

class TestImageLoader(unittest.TestCase):
    """
    Our basic test class
    """

    def test_save_images(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        saveImages('test_urls.txt')

        download_directory = os.path.join(PROJECT_ROOT, 'images')

        self.assertTrue(os.path.isfile(download_directory + '/padma-bridge_tFTLO5K.jpg'))


if __name__ == '__main__':
    unittest.main()