import unittest
import sys

module  = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global organiza_avaliacao
        undertest = __import__(module)
        organiza_avaliacao = getattr(undertest, 'organiza_avaliacao', None)

    def test_basico(self):
        l = [("Pedro", 1), ("Tito", -1), ("Zeca", 1), ("Lucca", -1),
("Mirna", 0)]
        assert organiza_avaliacao(l) == None
        assert l == [("Tito", -1), ("Lucca", -1), ("Mirna", 0), ("Pedro",
1), ("Zeca", 1)]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
