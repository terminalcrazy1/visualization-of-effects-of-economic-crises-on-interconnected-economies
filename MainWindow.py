from ClickableScene import ClickableScene
from GridPoint import GridPoint
from PyQt6.QtWidgets import (
    QGraphicsView, QGridLayout, QVBoxLayout,
    QLabel, QPushButton, QWidget
)
from random import randint
from typing import List

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
