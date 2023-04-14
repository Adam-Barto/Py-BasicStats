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

    def test_zmean(self):
        test_cases = [[[1.0, 2.0, 3.0, 4.0, 5.0], 3.0],
                [[13, 20, 32, 41], 26.5],
                [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 3.5]
                ]
        for (data, expected) in test_cases:
            with self.subTest(f"{data}, {expected}"):
                actual = szcw.zmean(data)
                Test.assertEqual(self, expected, actual)

    def test_zmode(self):
        test_cases = [[[1.0, 2.0, 2.0, 4.0, 5.0], 2.0],
                [[13, 20, 20, 41], 20.0],
                [[3.0, 2.0, 2.0, 4.0, 3.0, 3.0], 3.0]
                ]
        for (data, expected) in test_cases:
            with self.subTest(f"{data}, {expected}"):
                actual = szcw.zmode(data)
                Test.assertEqual(self, expected, actual)

    def test_zmedian(self):
        test_cases = [[[1.0, 2.0, 2.0, 4.0, 5.0], 2.0],
                [[13, 20, 30, 40, 50, 60], 35.0],
                [[7.0, 2.0, 2.0, 8.0, 6.0, 3.0], 4.5]
                ]
        for (data, expected) in test_cases:
            with self.subTest(f"{data}, {expected}"):
                actual = szcw.zmedian(data)
                Test.assertEqual(self, expected, actual)

    def test_zvariance(self):
        test_cases = [[[1.0, 2.0, 3.0, 4.0, 5.0], 2.5],
                [[13, 20, 30, 40, 50, 60], 321.5],
                [[7.0, 2.0, 2.0, 8.0, 6.0, 3.0], 7.0666667]
                ]
        for (data, expected) in test_cases:
            with self.subTest(f"{data}, {expected}"):
                actual = szcw.zvariance(data)
                Test.assertAlmostEqual(self, expected, actual, delta=.00001)

    def test_zstddev(self):
        test_cases = [[[1.0, 2.0, 3.0, 4.0, 5.0], 1.58113883],
                [[13, 20, 30, 40, 50, 60], 17.9304],
                [[7.0, 2.0, 2.0, 8.0, 6.0, 3.0], 2.65832027]
                ]
        for (data, expected) in test_cases:
            with self.subTest(f"{data}, {expected}"):
                actual = szcw.zstddev(data)
                Test.assertAlmostEqual(self, expected, actual, delta=.001)

    def test_zstderr(self):
        test_cases = [[[1.0, 2.0, 3.0, 4.0, 5.0], 0.707106781],
                [[13, 20, 30, 40, 50, 60], 7.320063751],
                [[7.0, 2.0, 2.0, 8.0, 6.0, 3.0], 1.085254706]
                ]
        for (data, expected) in test_cases:
            with self.subTest(f"{data}, {expected}"):
                actual = szcw.zstderr(data)
                Test.assertAlmostEqual(self, expected, actual, delta=.001)

    def test_zcorr(self):
        test_cases = [
            [[1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 2.0, 4.0, 5.0], 0.962],
            [[82, 43, 20, 4.0, 5.0], [1.0, 2.0, 8.0, 4.0, 9.0], -0.751],
            [[1.0, 2.0, 3.0, 6.0, 6.0], [2.0, 2.0, 4.0, 4.0, 8.0], 0.797]
            ]
        for (data0, data1, expected) in test_cases:
            with self.subTest(f'{data0}, {data1}, {expected}'):
                actual = szcw.zcorr(data0, data1)
                Test.assertAlmostEqual(self, expected, actual, delta=.001)
