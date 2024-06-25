def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def division(x,y):
    if y == 0:
        return 'Error: No se puede hacer una division con denominador cero'
    else:
        return x/y
    
def multiplicacion(x,y):
    return x*y

import unittest
class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(1, 2), 3)
        self.assertEqual(suma(-1, -2), -3)

    def test_resta(self):
        self.assertEqual(resta(1, 2), -1)
        self.assertEqual(resta(-1, -2), 1)

    def test_division(self):
        self.assertEqual(division(1, 2), 0.5)
        self.assertEqual(division(-1, 2), -0.5)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(1, 2), 2)
        self.assertEqual(multiplicacion(-1, 2), -2)

if __name__ == '__main__':
    unittest.main() 