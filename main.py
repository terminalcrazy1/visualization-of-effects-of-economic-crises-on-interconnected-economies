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
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Earth Is Flat")
        self.setFixedSize(800, 450)

        scene = QGraphicsScene(0, 0, 500, 420)

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