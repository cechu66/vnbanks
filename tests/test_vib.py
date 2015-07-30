import unittest
import vnbanks.banks.vib as vib


class TestVIB(unittest.TestCase):
    def test_interest_rate(self):
        rate = vib.VIB()
        self.assertTrue(rate.deposit_rate()['ONE_MONTH'] > 0)


if __name__ == '__main__':
    unittest.main()
