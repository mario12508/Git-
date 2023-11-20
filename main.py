import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random


class CirclePainter(QMainWindow):
    def __init__(self):
        super(CirclePainter, self).__init__()

        loadUi('UI.ui', self)

        self.generate_btn.clicked.connect(self.generate_circles)
        self.circles = []

    def generate_circles(self):
        # Создаем новый круг и добавляем его в список кругов
        diameter = random.randint(20, 100)
        color = QColor(Qt.yellow)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter, color))

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Очищаем экран, рисуя белый прямоугольник
        painter.fillRect(self.rect(), Qt.white)

        # Рисуем все круги из списка
        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    circle_painter = CirclePainter()
    window.setCentralWidget(circle_painter)
    window.setWindowTitle("MainWindow")
    window.setGeometry(0, 0, 608, 413)
    window.show()
    sys.exit(app.exec_())
