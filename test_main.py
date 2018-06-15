from unittest import TestCase
from main import main


class LenTest(TestCase):
    def test_basic_len(self):
        main_result = main()
        self.assertEqual(len(main_result[0]), 500)
        self.assertEqual(len(main_result[1]), 500)
        self.assertEqual(len(main_result[0]), len(main_result[1]))
