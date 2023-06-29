import unittest
from ClaseAnimal import Animal

class TestAnimal(unittest.TestCase):
    def test_CumplirAnios(self):
        a = Animal('perro', 'blanco')
        self.assertEqual(a.CumplirAnios(), 1)
        self.assertEqual(a.CumplirAnios(), 2)
        self.assertEqual(a.CumplirAnios(), 3)

    def test_ClaseAnimal_02(self):
        a = Animal('ballena','azul')
        for i in range(0,10):
            valor_test = a.CumplirAnios()
        valor_esperado = 10
        self.assertEqual(valor_test, valor_esperado)

    def test_ClaseAnimal_03(self):
        a = Animal('tortuga','verde')
        for i in range(0,100):
            valor_test = a.CumplirAnios()
        valor_esperado = 100
        self.assertEqual(valor_test, valor_esperado)

if __name__ == '__main__':
    unittest.main()
