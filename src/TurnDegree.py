class TurnDegree(object):
    def __init__(self, degree: int):
        self.degree = degree
        validList = [0,90,180,270,360]
        if not degree in validList:
            raise Exception("Invalid turn degree " + str(degree))
    def add(self, turnDegree):
        newDegree = self.degree + turnDegree.degree
        newDegree = (newDegree + 360) % 360
        return TurnDegree(newDegree)
    def min(self, turnDegree):
        newDegree = self.degree - turnDegree.degree
        newDegree = (newDegree + 360) % 360
        return TurnDegree(newDegree)
    def is90(self) -> bool:
        return self.degree == 90
    def is180(self) -> bool:
        return self.degree == 180
    def is270(self) -> bool:
        return self.degree == 270
    def is0(self) -> bool:
        return self.degree == 0
    def __str__(self):
        return "" + str(self.degree)