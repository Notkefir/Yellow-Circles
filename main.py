import sys
from random import randint
from design import Ui_Form
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qp = QPainter()
        self.pushButton.clicked.connect(self.clicked)
        self.should_paint_circle = False

    def clicked(self):
        self.should_paint_circle = True
        self.update()

    def paintEvent(self, event):
        if self.should_paint_circle:
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.qp.setBrush(QColor(255, 255, 0))
        if self.should_paint_circle:
            r = randint(20, 200)
            self.qp.drawEllipse(100, 100, r, r)


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
