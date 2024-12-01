import sys
import random
from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow

class AntiPlagiarism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_paint)
        self.painter = QPainter()
        self.flag = False

    def paintEvent(self, event):
        if self.flag:
            self.painter = QPainter()
            self.painter.begin(self)
            for _ in range(10):
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                self.painter.setBrush(QColor(r, g, b))
                radius = random.randint(0, 75)
                x, y = random.randint(100, 700), random.randint(50, 300)
                self.painter.drawEllipse(QPointF(x, y), radius, radius)
            self.painter.end()

    def start_paint(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AntiPlagiarism()
    ex.show()
    sys.exit(app.exec())
