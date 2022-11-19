import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint
from UI import Ui_MainWindow


class Circles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(x, y, d, d)

    def start_draw(self):
        self.draw = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
