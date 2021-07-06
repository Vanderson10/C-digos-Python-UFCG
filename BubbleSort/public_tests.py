import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global bubblestep
        undertest = __import__(module)
        bubblestep = getattr(undertest, 'bubblestep', None)

    def test_exemplo_1(self):
        dados = [4, 2, 1, 6, 3, 5]
        bubblestep(dados)
        assert dados == [2, 1, 4, 3, 5, 6]

    def test_exemplo_1(self):
        dados = [7, 3 ,1, 9, 6, 3]
        bubblestep(dados)
        assert dados == [3, 1, 7, 6, 3, 9]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
