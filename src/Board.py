try:
    from MarkedPosition import MarkedPosition
except (ModuleNotFoundError, ImportError):
    from .MarkedPosition import MarkedPosition

class Board(object):
    def __init__(self, ant, length:int):
        self.ant = ant
        self.length = length
        self.positions = []
        self.marked = {}
    def moveAnt(self):
        for x in range(self.length):
            position = self.ant.getPosition()
            if str(position) in self.marked:
                self.ant.forwardLeft()
                self.positions.append(MarkedPosition(False, position))
                del self.marked[str(position)]
            else:
                self.ant.forwardRight()
                self.positions.append(MarkedPosition(True, position))
                self.marked[str(position)] = position
    def getPositions(self):
        return self.positions