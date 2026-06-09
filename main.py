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
from PyQt6.QtCore import Qt

app = QApplication([])
last_point = (-10, -10)

def onMiddleClick(event):
    for pt in window.pts:
        if abs(pt.coords[0] - event.scenePos().x()) < 10 and abs(pt.coords[1] - event.scenePos().y()) < 10:
            print("Clicked on point at " + str(pt.coords) + " with load " + str(pt.load) + " and " + str(len(pt.links)) + " links")
            print(pt.links)
            return

def onRightClick(event):
    pass

def onLeftClick(event):
    global last_point
    if last_point != (-10, -10):
        for pt in window.pts:
            if abs(pt.coords[0] - last_point[0]) < 10 and abs(pt.coords[1] - last_point[1]) < 10:
                for pt2 in window.pts:
                    if abs(pt2.coords[0] - event.scenePos().x()) < 10 and abs(pt2.coords[1] - event.scenePos().y()) < 10:
                        pt.addLink(pt2)
                        pt2.addLink(pt)
                        print("Linked " + str(pt.coords) + " to " + str(pt2.coords))
                        last_point = (-10, -10)
                        break
                break
    else:
        last_point = (event.scenePos().x(), event.scenePos().y())
        print("last_point set")

class GridPoint():
    def __init__(self, coords: tuple[int, int]):
        self.coords = coords
        self.load = 0
        self.links = []

    def addLink(self, link: 'GridPoint'):
        self.links.append(link)
    
    def addLoad(self, load: int, previous = []):
        self.load += load
        for link in self.links:
            if link not in previous:
                link.addLoad(load * 0.15, previous + [self])

class ClickableScene(QGraphicsScene):
    def __init__(self, *args):
        super().__init__(*args)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            onLeftClick(event)
        elif event.button() == Qt.MouseButton.MiddleButton:
            onMiddleClick(event)
        elif event.button() == Qt.MouseButton.RightButton:
            onRightClick(event)

class MainWindow(QWidget):
    pts: list[GridPoint] = []

    def addDots(self, scene: QGraphicsScene):
        for x in range(1, 12):
            for y in range(1, 10):
                xmod = x * 40 + randint(-10, 10)
                ymod = y * 40 + randint(-10, 10)
                scene.addEllipse(xmod, ymod, 10, 10)
                pt = GridPoint((xmod, ymod))
                self.pts.append(pt)
    
    def resetScene(self, scene: QGraphicsScene):
        scene.clear()
        self.pts = []
        self.addDots(scene)

    def releaseWave(self):
        # self.pts[randint(0, len(self.pts)-1)].addLoad(randint(100, 500), None) 
        self.pts[0].addLoad(200)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Earth Is Flat")
        self.setFixedSize(800, 450)

        scene = ClickableScene(0, 0, 500, 420)
        self.addDots(scene)

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
        stack_layout.addStretch()

window = MainWindow()
window.show()
app.exec()