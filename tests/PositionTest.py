import unittest
from src.Position import Position

class PositionTest(unittest.TestCase):

    def test_position_left(self):
        position = Position(0,0)
        newPosition = position.left()
        self.assertEquals(-1, newPosition.getX())
        self.assertEquals(0, newPosition.getY())

    def test_position_right(self):
        position = Position(0, 0)
        newPosition = position.right()
        self.assertEquals(1, newPosition.getX())
        self.assertEquals(0, newPosition.getY())

    def test_position_down(self):
        position = Position(0, 0)
        newPosition = position.down()
        self.assertEquals(0, newPosition.getX())
        self.assertEquals(-1, newPosition.getY())

    def test_position_up(self):
        position = Position(0, 0)
        newPosition = position.up()
        self.assertEquals(0, newPosition.getX())
        self.assertEquals(1, newPosition.getY())

    def test_string(self):
        position = Position(0, 0)
        self.assertEquals("[0,0]", str(position))

if __name__ == '__main__':
    unittest.main()