import unittest
from src.Position import Position

class PositionTest(unittest.TestCase):

    def test_position_left(self):
        position = Position(0,0)
        newPosition = position.left()
        self.assertEqual(-1, newPosition.getX())
        self.assertEqual(0, newPosition.getY())

    def test_position_right(self):
        position = Position(0, 0)
        newPosition = position.right()
        self.assertEqual(1, newPosition.getX())
        self.assertEqual(0, newPosition.getY())

    def test_position_down(self):
        position = Position(0, 0)
        newPosition = position.down()
        self.assertEqual(0, newPosition.getX())
        self.assertEqual(-1, newPosition.getY())

    def test_position_up(self):
        position = Position(0, 0)
        newPosition = position.up()
        self.assertEqual(0, newPosition.getX())
        self.assertEqual(1, newPosition.getY())

    def test_string(self):
        position = Position(0, 0)
        self.assertEqual("[0,0]", str(position))

if __name__ == '__main__':
    unittest.main()