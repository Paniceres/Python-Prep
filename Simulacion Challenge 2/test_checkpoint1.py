import unittest
import os
import checkpoint1 as ch

class HenryChallenge(unittest.TestCase):
    def test_OrdenarDiccionario_01(self):
      dicc = {'clave1':['c','a','b'], 'clave2':['casa','auto','barco'], 'clave3':[3,1,2]}
      valor_test = ch.ordenarDiccionario(dicc, 'clave1')
      valor_esperado = {'clave1':['c','b','a'], 'clave2':['casa','barco','auto'], 'clave3':[3,2,1]}
      self.assertEqual(valor_test, valor_esperado)

    def test_OrdenarDiccionario_02(self):
      dicc = ['c','a','b']
      valor_test = ch.ordenarDiccionario(dicc, 'clave1', True)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_OrdenarDiccionario_03(self):
      dicc = {'clave1':['c','a','b'], 'clave2':['casa','auto','barco'], 'clave3':[3,1,2]}
      valor_test = ch.ordenarDiccionario(dicc, 'clave1', False)
      valor_esperado = {'clave1':['a','b','c'], 'clave2':['auto','barco','casa'], 'clave3':[1,2,3]}
      self.assertEqual(valor_test, valor_esperado)
      
resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

hc_tests = resultado_test.result.testsRun
hc_fallas = len(resultado_test.result.failures)
hc_errores = len(resultado_test.result.errors)
hc_ok = hc_tests - hc_fallas - hc_errores

archivo_test = open('resultado_test.csv', 'w')
archivo_test.write('Total_Tests,Total_Fallas,Total_Errores,Total_Correctos\n')
archivo_test.write(str(hc_tests)+','+str(hc_fallas)+','+str(hc_errores)+','+str(hc_ok)+'\n')
archivo_test.close()

print('Resumen')
print('Total Tests:', str(hc_tests))
print('Total Fallas:', str(hc_fallas))
print('Total Errores:', str(hc_errores))
print('Total Correctos:', str(hc_ok))
