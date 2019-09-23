import unittest
from src.Ant import Ant
from src.Position import Position
from src.TurnDegree import TurnDegree

class AntTest(unittest.TestCase):

    def test_ant_forward_left(self):
        ant = Ant(Position(0,0), TurnDegree(0))
        ant.forwardLeft()
        ant.forwardLeft()
        self.assertEqual("180", str(ant.getTurnDegree()))
        self.assertEqual("[0,0]", str(ant.getEventHistory()[0]))
        self.assertEqual("[-1,0]", str(ant.getEventHistory()[1]))
        self.assertEqual("[-1,-1]", str(ant.getEventHistory()[2]))

    def test_ant_forward_right(self):
        ant = Ant(Position(0,0), TurnDegree(0))
        ant.forwardRight()
        ant.forwardRight()
        self.assertEqual("180", str(ant.getTurnDegree()))
        self.assertEqual("[0,0]", str(ant.getEventHistory()[0]))
        self.assertEqual("[1,0]", str(ant.getEventHistory()[1]))
        self.assertEqual("[1,-1]", str(ant.getEventHistory()[2]))

    def test_ant_forward_right_and_left(self):
        ant = Ant(Position(0,0), TurnDegree(0))
        ant.forwardRight()
        ant.forwardRight()
        ant.forwardLeft()
        ant.forwardLeft()
        self.assertEqual("0", str(ant.getTurnDegree()))
        self.assertEqual("[0,0]", str(ant.getEventHistory()[0]))
        self.assertEqual("[1,0]", str(ant.getEventHistory()[1]))
        self.assertEqual("[1,-1]", str(ant.getEventHistory()[2]))
        self.assertEqual("[2,-1]", str(ant.getEventHistory()[3]))
        self.assertEqual("[2,0]", str(ant.getEventHistory()[4]))

if __name__ == '__main__':
    unittest.main()