import unittest
import aritimetic
#arquivo a ser executado para os testes
class Test_soma(unittest.TestCase):
    def test_soma_int(self):
        soma = aritimetic.soma(50,50)
        self.assertEqual(soma,100)
    def test_soma_float(self):
        soma = aritimetic.soma(2.5,2.5)
        self.assertEqual(soma,5.0)
    def test_soma_string(self):
        soma = aritimetic.soma("Rodrigo"," Dutra")
        self.assertEqual(soma,"Rodrigo Dutra")


if __name__ == '__main__':
    unittest.main()