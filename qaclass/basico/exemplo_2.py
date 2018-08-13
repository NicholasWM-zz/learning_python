"""Base de Testes"""
from unittest import TestCase, main


def add(x,y):
    '''Funcao de adicao soma dois valores'''
    return x + y


# assert add(7,7) == 15, "o valor da soma esta errado"

class TestAdd(TestCase):
    def test_soma_deve_retornar_14(self):
        entrada = add(7,7)
        esperado = 15
        self.assertEqual(entrada, esperado)

        self.asser
if __name__ == "__main__":
    main()
