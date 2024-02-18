import unittest

from operaciones import *

class TestSumar(unittest.TestCase):
 
 def test_sumar(self):

    self.assertEqual(sumar(3, 2), 5)
    self.assertEqual(sumar(-3,3), 0)
    self.assertEqual(sumar(-3,-2), -5)

    self.assertEqual(restar(8, 3), 5)
    self.assertEqual(restar(3, 3), 0)
    self.assertEqual(restar(-8, 2), -10)

    self.assertEqual(multiplicar(5, 1), 5)
    self.assertEqual(multiplicar(5, 0), 0)
    self.assertEqual(multiplicar(-5, 1), -5)

    self.assertEqual(dividir(10,2), 5)
    self.assertEqual(dividir(5,2), 2)
    self.assertEqual(dividir(-10,2), -5)

if __name__ == '__main__':
 unittest.main()