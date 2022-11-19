import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint
from PyQt5 import uic


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.addCircleButton.clicked.connect(self.start_draw)
        self.draw = False

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()

    def drawCircle(self, qp):
        y = randint(60, self.height() - 40)
        x = randint(0, self.width() - 40)
        d = randint(10, 500)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, d, d)

    def start_draw(self):
        self.draw = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
