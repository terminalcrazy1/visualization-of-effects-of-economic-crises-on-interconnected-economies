from typing import Any, List, Optional
from random import randint
from PyQt6.QtWidgets import (
    QApplication, QGraphicsScene, QGraphicsView, QGridLayout,
    QVBoxLayout, QPushButton, QLabel, QWidget, QGraphicsEllipseItem,
    QGraphicsLineItem, QGraphicsSceneMouseEvent
)
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtCore import Qt

class GridPoint:
    previous: List['GridPoint'] = []

    def __init__(self, coords: tuple[int, int], visual: QGraphicsEllipseItem, window: Optional['MainWindow'] = None) -> None:
        self.coords: tuple[int, int] = coords
        self.load: float = 0
        self.links: List['GridPoint'] = []
        self.lines: List[QGraphicsLineItem] = []
        self.visual: QGraphicsEllipseItem = visual
        self.window: Optional['MainWindow'] = window

    def addLink(self, link: 'GridPoint') -> None:
        self.links.append(link)
    
    def addLoad(self, load: float) -> None:
        ct = 0
        for link in list(self.links):
            if link not in self.previous:
                self.previous.append(link)
                link.addLoad(load * 0.15)
                ct += 1
        if ct >= 6:
            self.load += load * 0.1
        else:
            self.load += load * (1 - (0.15 * ct))
        if self.load >= 100:
            self.load = 100
            for link in list(self.links):
                if link.load < 100:
                    link.addLoad(100 - link.load)
                if self in link.links:
                    link.links.remove(self)
            for line in self.lines:
                if line.scene():
                    line.scene().removeItem(line)
            if self.visual.scene():
                self.visual.scene().removeItem(self.visual)
            if self.window and self in self.window.pts:
                self.window.pts.remove(self)

class ClickableScene(QGraphicsScene):
    def __init__(self, parent_window: 'MainWindow', *args: Any) -> None:
        super().__init__(*args)
        self.window: 'MainWindow' = parent_window
        self.last_point: Optional[GridPoint] = None
    
    def get_pt_at(self, event: QGraphicsSceneMouseEvent) -> Optional[GridPoint]:
        pos = event.scenePos()
        for pt in self.window.pts:
            if abs(pt.coords[0] - pos.x()) < 10 and abs(pt.coords[1] - pos.y()) < 10:
                return pt
        return None

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        pt = self.get_pt_at(event)
        if not pt: return

        if event.button() == Qt.MouseButton.LeftButton:
            if self.last_point:
                pt2 = pt
                pt1 = self.last_point
                pt1.addLink(pt2)
                pt2.addLink(pt1)
                line = self.addLine(pt1.coords[0]+5, pt1.coords[1]+5, pt2.coords[0]+5, pt2.coords[1]+5)
                pt1.lines.append(line)
                pt2.lines.append(line)
                self.last_point = None
            else:
                self.last_point = pt
                
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.window.load_indicator.setText("Load: " + str(pt.load))
            
        elif event.button() == Qt.MouseButton.RightButton:
            self.window.origin = self.window.pts.index(pt)

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.pts: List[GridPoint] = []
        self.origin: int = 0
        self.setWindowTitle("The Earth Is Flat")
        self.setFixedSize(800, 450)

        self.scene: ClickableScene = ClickableScene(self, 0, 0, 500, 420)
        self.addDots(self.scene)

        view = QGraphicsView(self.scene)
        layout = QGridLayout()
        self.setLayout(layout)

        stack = QWidget()
        stack_layout = QVBoxLayout()
        stack.setLayout(stack_layout)

        layout.addWidget(stack, 0, 4, 2, 4)
        layout.addWidget(view, 0, 0, 4, 4)
        
        release_button = QPushButton("Release Wave")
        reset_button = QPushButton("Reset")
        self.load_indicator: QLabel = QLabel("Load: ")
        
        release_button.clicked.connect(self.releaseWave)
        reset_button.clicked.connect(lambda: self.resetScene(self.scene))

        stack_layout.addWidget(release_button)
        stack_layout.addWidget(reset_button)
        stack_layout.addWidget(self.load_indicator)
        stack_layout.addStretch()

    def addDots(self, scene: ClickableScene) -> None:
        for x in range(1, 12):
            for y in range(1, 10):
                xmod = x * 40 + randint(-10, 10)
                ymod = y * 40 + randint(-10, 10)
                visual = scene.addEllipse(xmod, ymod, 10, 10)
                self.pts.append(GridPoint((xmod, ymod), visual, self))
    
    def resetScene(self, scene: ClickableScene) -> None:
        scene.clear()
        self.pts = []
        self.addDots(scene)

    def releaseWave(self) -> None:
        self.pts[self.origin].previous = []
        self.pts[self.origin].addLoad(50) 

app = QApplication([])
window = MainWindow()
window.show()
app.exec()