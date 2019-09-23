import unittest
from src.TurnDegree import TurnDegree

class TurnDegreeTest(unittest.TestCase):

    def test_construct(self):
        TurnDegree(0)

    def test_invalid(self):
        thrown: bool = False
        try:
            TurnDegree(1)
        except:
            thrown = True
        self.assertTrue(thrown)

    def test_add(self):
        degree = TurnDegree(0)
        self.assertEqual("90", str(degree.add(TurnDegree(90))))
        self.assertEqual("180", str(
                degree
                    .add(TurnDegree(90))
                    .add(TurnDegree(90))
                    .add(TurnDegree(90))
                    .add(TurnDegree(90))
                    .add(TurnDegree(90))
                    .add(TurnDegree(90))
            )
        )

    def test_min(self):
        degree = TurnDegree(0)
        self.assertEqual("270", str(degree.min(TurnDegree(90))))
        self.assertTrue(
            degree
                .min(TurnDegree(90))
                .min(TurnDegree(90))
                .min(TurnDegree(90))
                .min(TurnDegree(90))
                .min(TurnDegree(90))
                .min(TurnDegree(90))
                .is180()
        )

if __name__ == '__main__':
    unittest.main()