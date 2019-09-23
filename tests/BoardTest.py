import unittest
from src.Position import Position
from src.Ant import Ant
from src.Board import Board
from src.TurnDegree import TurnDegree

class BoardTest(unittest.TestCase):

    def test_move_6_times(self):
        ant = Ant(Position(0,0), TurnDegree(0))
        board = Board(ant, 6)
        board.moveAnt()

        marked = board.getPositions()
        self.assertEqual("[0,0]", str(marked[0].getPosition()))
        self.assertEqual(True, marked[0].isMarked())
        self.assertEqual("[1,0]", str(marked[1].getPosition()))
        self.assertEqual(True, marked[1].isMarked())
        self.assertEqual("[1,-1]", str(marked[2].getPosition()))
        self.assertEqual(True, marked[2].isMarked())
        self.assertEqual("[0,-1]", str(marked[3].getPosition()))
        self.assertEqual(True, marked[3].isMarked())
        self.assertEqual("[0,0]", str(marked[4].getPosition()))
        self.assertEqual(False, marked[4].isMarked())
        self.assertEqual("[-1,0]", str(marked[5].getPosition()))
        self.assertEqual(True, marked[5].isMarked())

if __name__ == '__main__':
    unittest.main()