from random import randint
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsScene,
    QGraphicsView,
    QGridLayout,
    QVBoxLayout,
    QPushButton,
    QWidget
)

app = QApplication([])

def onMiddleClick(event):
    pass

def onRightClick(event):
    pass

def onLeftClick(event):
    pass

class ClickableScene(QGraphicsScene):
    def init(self, args):
        super().__init__(args)
    
    def mousePressEvent(self, event):
        print(str(event.scenePos()))
    

class MainWindow(QWidget):
    def addDots(self, scene: QGraphicsScene):
        for x in range(1,12):
            for y in range(1,10):
                xmod = x * 40 + randint(-10,10)
                ymod = y * 40 + randint(-10,10)
                scene.addEllipse(xmod, ymod, 10, 10)
    
    def resetScene(self, scene: QGraphicsScene):
        scene.clear()
        self.addDots(scene)

    def releaseWave(self):
        pass

    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Earth Is Flat")
        self.setFixedSize(800, 450)

        scene = ClickableScene(0, 0, 500, 420)
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
        
        release_button = QPushButton("Release Wave")
        reset_button = QPushButton("Reset")
        release_button.clicked.connect(self.releaseWave)
        reset_button.clicked.connect(lambda: self.resetScene(scene))

        stack_layout.addWidget(release_button)
        stack_layout.addWidget(reset_button)
        stack_layout.addStretch() # top align widgets

window = MainWindow()
window.show()

app.exec()