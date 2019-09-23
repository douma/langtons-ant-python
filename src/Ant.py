from TurnDegree import TurnDegree

class Ant(object):
    def __init__(self, position, turnDegree):
        self.position = position
        self.degree = turnDegree
        self.eventHistory = []
        self.eventHistory.append(self.position)
    def forwardLeft(self):
        self.degree = self.degree.min(TurnDegree(90))
        self._updatePosition()
    def forwardRight(self):
        self.degree = self.degree.add(TurnDegree(90))
        self._updatePosition()
    def _updatePosition(self):
        if self.degree.is0():
            self.position = self.position.up()
        elif self.degree.is90():
            self.position = self.position.right()
        elif self.degree.is180():
            self.position = self.position.down()
        elif self.degree.is270():
            self.position = self.position.left()
        else:
            raise Exception("Cannot calculate position for degree " + str(self.degree))
        self.eventHistory.append(self.position)
    def getTurnDegree(self):
        return self.degree
    def getEventHistory(self):
        return self.eventHistory
    def getPosition(self):
        return self.position