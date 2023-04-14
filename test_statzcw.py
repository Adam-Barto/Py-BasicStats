from unittest import TestCase
import statzcw as szcw

class Test(TestCase):
    def test_zcount(self):
        test_cases = [[[1.0, 2.0, 3.0, 4.0, 5.0], 5.0],
                [[13, 20, 32, 41], 4.0],
                [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 6.0]
                ]
        for (data, expected) in test_cases:
            with self.subTest(f"{data}, {expected}"):
                actual = szcw.zcount(data)
                Test.assertEqual(self, expected, actual)

