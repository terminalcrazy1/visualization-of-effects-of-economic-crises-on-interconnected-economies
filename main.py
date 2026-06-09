from random import randint
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsScene,
    QGraphicsView,
    QGridLayout,
    QVBoxLayout,
    QWidget
)

app = QApplication([])

class MainWindow(QWidget):
    def addDots(self, scene: QGraphicsScene):
        for x in range(1,12):
            for y in range(1,10):
                xmod = x * 40 + randint(-10,10)
                ymod = y * 40 + randint(-10,10)
                scene.addEllipse(xmod, ymod, 10, 10)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Earth Is Flat")
        self.setFixedSize(800, 450)

        scene = QGraphicsScene(0, 0, 500, 420)
        self.addDots(scene)

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