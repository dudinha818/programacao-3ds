# test_calculadora.py
import unittest
from calculadora import soma, subtrai, multiplica, divide

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        casos = [
            (1, 2, 3, "Soma de 1 + 2 deve ser 3"),
            (-1, 1, 0, "Soma de -1 + 1 deve ser 0"),
            (-1, -1, -2, "Soma de -1 + -1 deve ser -2"),
        ]
        for a, b, esperado, msg in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(soma(a, b), esperado, msg)

    def test_subtrai(self):
        casos = [
            (10, 5, 5, "Subtração de 10 - 5 deve ser 5"),
            (-1, -1, 0, "Subtração de -1 - (-1) deve ser 0"),
            (0, 1, -1, "Subtração de 0 - 1 deve ser -1"),
        ]
        for a, b, esperado, msg in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(subtrai(a, b), esperado, msg)

    def test_multiplica(self):
        casos = [
            (3, 7, 21, "Multiplicação de 3 * 7 deve ser 21"),
            (-1, 1, -1, "Multiplicação de -1 * 1 deve ser -1"),
            (0, 10, 0, "Multiplicação de 0 * 10 deve ser 0"),
        ]
        for a, b, esperado, msg in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(multiplica(a, b), esperado, msg)

    def test_divide(self):
        casos = [
            (10, 2, 5, "Divisão de 10 / 2 deve ser 5"),
            (-10, 2, -5, "Divisão de -10 / 2 deve ser -5"),
        ]
        for a, b, esperado, msg in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(divide(a, b), esperado, msg)

        # Teste de divisão por zero
        with self.assertRaises(ValueError, msg="Divisão por zero deve gerar ValueError"):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
