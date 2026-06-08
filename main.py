from random import randint
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsEllipseItem,
    QGridLayout,
    QVBoxLayout,
    QWidget
)
from PyQt6.QtGui import QBrush
from PyQt6.QtCore import Qt

app = QApplication([])

class ClickableScene(QGraphicsScene):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Earth Is Flat")
        self.setFixedSize(800, 450)

        scene = ClickableScene()

        """
        column width (125px)
        row width (105px)
        = grid size 750px * 420px
        """
        view = QGraphicsView(scene)
        
        layout = QGridLayout()
        self.setLayout(layout)

        stack = QWidget()
        stack_layout = QVBoxLayout()
        stack.setLayout(stack_layout)

        layout.addWidget(stack, 0, 4, 2, 4)
        layout.addWidget(view, 0, 0, 4, 4)

        # add stack widgets here



window = MainWindow()
window.show()

app.exec()