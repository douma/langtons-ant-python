class Position():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def left(self):
        return Position(self.x -1, self.y)
    def right(self):
        return Position(self.x +1, self.y)
    def up(self):
        return Position(self.x, self.y+1)
    def down(self):
        return Position(self.x, self.y-1)
    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]";
