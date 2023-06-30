import unittest
import checkpoint as ch

class PruebaHenryChallenge(unittest.TestCase):

    def test_EncontrarMayores_01(self):
        lista = [1, 5, 10, 15, 20]
        n = 10
        valor_test = ch.EncontrarMayores(lista, n)
        valor_esperado = [15, 20]
        self.assertEqual(valor_test, valor_esperado)

    def test_EncontrarMayores_02(self):
        lista = [2, 4, 6, 8, 10]
        n = 7
        valor_test = ch.EncontrarMayores(lista, n)
        valor_esperado = [8, 10]
        self.assertEqual(valor_test, valor_esperado)

    def test_EncontrarMayores_03(self):
        lista = [3, 6, 9, 12, 15]
        n = 20
        valor_test = ch.EncontrarMayores(lista, n)
        valor_esperado = []
        self.assertEqual(valor_test, valor_esperado)

    def test_SumarIterador_01(self):
        iterable = [1, 2, 3, 4, 5]
        valor_test = ch.SumarIterador(iterable)
        valor_esperado = 15
        self.assertEqual(valor_test, valor_esperado)

    def test_SumarIterador_02(self):
        iterable = [10, 20, 30, 40, 50]
        valor_test = ch.SumarIterador(iterable)
        valor_esperado = 150
        self.assertEqual(valor_test, valor_esperado)

    def test_SumarIterador_03(self):
        iterable = [0, -1, 2, -3, 4]
        valor_test = ch.SumarIterador(iterable)
        valor_esperado = 2
        self.assertEqual(valor_test, valor_esperado)

    def test_FiltrarPalabras_01(self):
        lista_palabras = ['Python', 'Java', 'JavaScript', 'C++', 'Ruby']
        letra = 'J'
        valor_test = ch.FiltrarPalabras(lista_palabras, letra)
        valor_esperado = ['Java', 'JavaScript']
        self.assertEqual(valor_test, valor_esperado)

    def test_FiltrarPalabras_02(self):
        lista_palabras = ['Hola', 'Adiós', 'Hambre', 'Sed', 'Hamaca']
        letra = 'H'
        valor_test = ch.FiltrarPalabras(lista_palabras, letra)
        valor_esperado = ['Hola', 'Hambre', 'Hamaca']
        self.assertEqual(valor_test, valor_esperado)

    def test_FiltrarPalabras_03(self):
        lista_palabras = ['Python', 'Java', 'JavaScript', 'C++', 'Ruby']
        letra = 'P'
        valor_test = ch.FiltrarPalabras(lista_palabras, letra)
        valor_esperado = ['Python']
        self.assertEqual(valor_test, valor_esperado)

resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

hc_tests = resultado_test.result.testsRun
hc_fallas = len(resultado_test.result.failures)
hc_errores = len(resultado_test.result.errors)
hc_ok = hc_tests
