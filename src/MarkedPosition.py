from . import Position

class MarkedPosition():
    marked = False
    def __init__(self, marked: bool, position: Position):
        self.marked = marked
        self.position = position
    def isMarked(self) -> bool:
        return self.marked
    def position(self) -> Position:
        return self.position