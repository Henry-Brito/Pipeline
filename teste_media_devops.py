import unittest
from media_devops import valor_minimo_p2

class TestValorMinimoP2(unittest.TestCase):

    def test_valor_minimo_p2_case1(self):
        self.assertAlmostEqual(valor_minimo_p2(q2=8.33, p1=4, n2=9.5), 7.55, places=2)

if __name__ == '__main__':
    unittest.main()
