from MainWindow import MainWindow
from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsLineItem
from typing import List, Optional

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