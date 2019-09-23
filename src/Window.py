from tkinter import Tk, Canvas, Frame, BOTH

from Ant import Ant
from TurnDegree import TurnDegree
from Position import Position
from Board import Board

class Window(Frame):
    def __init__(self, board, root):
        super().__init__()

        self.master.title("Langton's ant")
        self.pack(fill=BOTH, expand=0)
        canvas = Canvas(root, width=800, height=800)

        for position in board.getPositions():
            if position.isMarked():
                canvas.create_line(
                    position.getPosition().getX(),
                    position.getPosition().getY(),
                    position.getPosition().getX() + 1,
                    position.getPosition().getY() + 1,
                    fill="#000000")
            else:
                canvas.create_line(
                    position.getPosition().getX(),
                    position.getPosition().getY(),
                    position.getPosition().getX() + 1,
                    position.getPosition().getY() + 1,
                    fill="#ffffff")

        canvas.pack(fill=BOTH, expand=0)

def main():
    root = Tk()

    ant = Ant(Position(530, 530), TurnDegree(0))
    board = Board(ant, 36000)
    board.moveAnt()

    Window(board, root)
    root.geometry("800x800")
    root.mainloop()

if __name__ == '__main__':
    main()