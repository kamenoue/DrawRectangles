import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication,QWidget 

class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.accumpos = []
        self.setMinimumSize(500, 500)
        self.setMaximumSize(500, 500)
        self.startpos = QPoint(0,0)
        self.endpos = QPoint(0,0)

    def mousePressEvent(self, event):
        self.startpos = event.pos()

    def mouseMoveEvent(self, event):
        self.endpos = event.pos()
        self.update()


    def mouseReleaseEvent(self, event):
        self.endpos = event.pos()
        self.accumpos.append([self.startpos, self.endpos])
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.accumpos = []
            self.startpos = QPoint(0,0)
            self.endpos = QPoint(0,0)
            self.update()        

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.black)

        painter.setBrush(QColor(100,100,255,100))
        for startpos,endpos in self.accumpos:
            painter.drawRect(startpos.x(), startpos.y(), endpos.x()-startpos.x(), endpos.y()-startpos.y())

        painter.drawRect(self.startpos.x(), self.startpos.y(), self.endpos.x()-self.startpos.x(), self.endpos.y()-self.startpos.y())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.setWindowTitle('DrawRectangles')
    w.show()
    sys.exit(app.exec_())

