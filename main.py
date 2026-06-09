from time import sleep
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
    event.scenePos()

def onRightClick(event):
    pass

def onLeftClick(event):
    pass

class GridPoint():
    load: int = 0
    coords: tuple[int] = ()
    links: list[GridPoint] = []

    def init(self, constructed_coords: tuple[int]):
        self.coords = constructed_coords

    def addLink(self, link: GridPoint):
        self.links.append(link)
    
    def addLoad(self, load: int):
        self.load += load
        for link in self.links:
            link.addLoad(load * 0.15)


class ClickableScene(QGraphicsScene):
    def init(self, args):
        super().__init__(args)
    
    def mousePressEvent(self, event):
        for pt in window.pts:
            if abs(pt.coords[0] - event.scenePos().x()) < 10 and abs(pt.coords[1] - event.scenePos().y()) < 10:
                print("Clicked on point at " + str(pt.coords) + " with load " + str(pt.load) + " and " + str(len(pt.links)) + " links")
                return
    

class MainWindow(QWidget):

    pts: list[GridPoint] = []

    def addDots(self, scene: QGraphicsScene):
        for x in range(1,12):
            for y in range(1,10):
                xmod = x * 40 + randint(-10,10)
                ymod = y * 40 + randint(-10,10)
                scene.addEllipse(xmod, ymod, 10, 10)
                pt = GridPoint()
                pt.init((xmod, ymod))
                self.pts.append(pt)
                
    
    def resetScene(self, scene: QGraphicsScene):
        scene.clear()
        self.pts = []
        self.addDots(scene)

    def releaseWave(self):
        self.pts[randint(0, len(self.pts)-1)].addLoad(randint(100, 500))

    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Earth Is Flat")
        self.setFixedSize(800, 450)

        scene = ClickableScene(0, 0, 500, 420)

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