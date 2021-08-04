from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QFont, QBrush, QPolygon, QPainterPath
from PyQt5.QtCore import Qt, QRect, QPoint
from shapely.geometry import Point


import sys, time

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.text = "Welcome to Summoner's Rift"
        self.setGeometry(600, 300, 500, 500)
        self.setWindowTitle('Painter')

    def paintEvent(self, event):

        pt = QPainter(self)

        path = [Point(100, 100), Point(400, 300)]
        pt.drawPath(path)



app = QApplication(sys.argv)
ui = UI()
ui.show()
sys.exit(app.exec_())




